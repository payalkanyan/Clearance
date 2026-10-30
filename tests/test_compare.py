"""Stage 7: the diff reports differences instead of explaining them away."""

from __future__ import annotations

import json

import pytest

from clearance import compare as compare_module
from clearance.compare import compare, report, similarity
from clearance.schema import Difficulty, Fact, Guide, Label, Meta, Source, Verified


def fact(text: str, label: Label = Label.SOURCED) -> dict:
    payload = {"text": text, "label": label.value}
    if label is Label.SOURCED:
        payload |= {"source_url": "https://docs.example.com/a", "quote": text[:40]}
    return payload


def guide_payload(*, difficulty: str, provenance: str, **sections) -> dict:
    base = {
        "app_name": "Example",
        "website": "example.com",
        "verdict": fact("Self-serve with no review"),
        "difficulty": difficulty,
        "hands_on_time": {"text": "5 to 15 minutes", "label": "Inferred"},
        "waiting_time": {"text": "None", "label": "Inferred"},
        "composio_status": {"text": "Managed", "label": "Inferred"},
        "prerequisites": [fact("An account")],
        "setup_steps": [fact("Open the console")],
        "limits_before_approval": [fact("No limits")],
        "approval_process": [fact("No review")],
        "likely_blockers": [fact("Rate limits apply")],
        "open_questions": [{"text": "Unknown quota", "label": "Uncertain"}],
        "sources": [{"url": "https://docs.example.com/a"}],
        "last_verified": {"date": "2026-10-30", "by": "human" if provenance == "human-gold" else "agent"},
        "meta": {"slug": "example", "provenance": provenance},
    }
    base.update(sections)
    return base


@pytest.fixture
def guides(tmp_path, monkeypatch):
    monkeypatch.setattr(compare_module, "GUIDES_DIR", tmp_path)

    def write(gold: dict, agent: dict):
        (tmp_path / "example.json").write_text(json.dumps(gold))
        (tmp_path / "example.agent.json").write_text(json.dumps(agent))

    return write


def test_content_word_overlap_beats_a_bare_character_ratio():
    short = "A GitHub account"
    long = "A personal GitHub account or administrative access to a GitHub organization."
    assert similarity(short, long) >= 0.45


def test_unrelated_sentences_do_not_match():
    assert similarity(
        "None; there is no approval step for OAuth apps.",
        "A user or organization can own up to 100 OAuth apps.",
    ) < 0.45


def test_single_value_fields_always_pair_and_flag_divergence(guides):
    guides(
        guide_payload(difficulty="Easy", provenance="human-gold"),
        guide_payload(
            difficulty="Easy",
            provenance="agent",
            waiting_time={"text": "Immediate for standard apps, unknown for marketplace",
                          "label": "Inferred"},
        ),
    )
    result = compare("example")
    waiting = next(p for p in result.matched if p.section == "waiting_time")
    assert waiting.weak is True
    assert "Same field, wording far apart" in report(result)


def test_missing_and_extra_facts_are_both_reported(guides):
    guides(
        guide_payload(
            difficulty="Easy",
            provenance="human-gold",
            likely_blockers=[fact("An organisation owner must approve the app")],
        ),
        guide_payload(
            difficulty="Easy",
            provenance="agent",
            likely_blockers=[fact("The app cannot be your sole identity provider")],
        ),
    )
    result = compare("example")
    assert any("organisation owner" in item.text for item in result.missing)
    assert any("sole identity provider" in item.text for item in result.extra)


def test_a_gold_tested_step_the_agent_missed_is_not_counted_as_a_failure(guides):
    guides(
        guide_payload(
            difficulty="Easy",
            provenance="human-gold",
            setup_steps=[fact("Click Generate a new client secret", Label.TESTED)],
        ),
        guide_payload(difficulty="Easy", provenance="agent", setup_steps=[fact("Open the console")]),
    )
    result = compare("example")
    assert [item.text for item in result.human_only_missing] == [
        "Click Generate a new client secret"
    ]
    assert result.missing == []


def test_a_relabelled_tested_step_lands_in_the_human_only_bucket(guides):
    guides(
        guide_payload(
            difficulty="Easy",
            provenance="human-gold",
            setup_steps=[fact("Click Register application and copy the Client ID", Label.TESTED)],
        ),
        guide_payload(
            difficulty="Easy",
            provenance="agent",
            setup_steps=[fact("Click Register application to create the OAuth app")],
        ),
    )
    result = compare("example")
    assert len(result.human_only_labels) == 1
    assert result.label_differences == []


def test_a_real_label_difference_is_reported(guides):
    guides(
        guide_payload(difficulty="Easy", provenance="human-gold"),
        guide_payload(
            difficulty="Easy",
            provenance="agent",
            verdict={"text": "Self-serve with no review", "label": "Inferred"},
        ),
    )
    result = compare("example")
    difference = next(p for p in result.label_differences if p.section == "verdict")
    assert difference.gold_label is Label.SOURCED
    assert difference.agent_label is Label.INFERRED


def test_difficulty_mismatch_is_stated_not_smoothed(guides):
    guides(
        guide_payload(difficulty="Easy", provenance="human-gold"),
        guide_payload(difficulty="Hard", provenance="agent"),
    )
    result = compare("example")
    assert result.difficulty_agrees is False
    assert "MISMATCH" in report(result)


def test_each_gold_fact_matches_at_most_one_agent_fact(guides):
    guides(
        guide_payload(
            difficulty="Easy",
            provenance="human-gold",
            prerequisites=[fact("An account"), fact("An account")],
        ),
        guide_payload(difficulty="Easy", provenance="agent", prerequisites=[fact("An account")]),
    )
    result = compare("example")
    assert len([p for p in result.matched if p.section == "prerequisites"]) == 1
    assert len([m for m in result.missing if m.section == "prerequisites"]) == 1


def test_a_missing_agent_guide_is_an_error(guides, tmp_path, monkeypatch):
    monkeypatch.setattr(compare_module, "GUIDES_DIR", tmp_path)
    (tmp_path / "nothing.json").write_text(
        json.dumps(guide_payload(difficulty="Easy", provenance="human-gold"))
    )
    with pytest.raises(FileNotFoundError, match="no agent guide"):
        compare("nothing")
