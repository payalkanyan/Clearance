"""The schema rules that keep a guide honest."""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from clearance.config import slugify
from clearance.schema import Fact, Guide, Label, load_guide

GOLD = "guides/github.json"


def agent_fact(**kwargs) -> Fact:
    return Fact(**kwargs)


def minimal_guide(**overrides) -> dict:
    sourced = {
        "text": "You can register an app without review",
        "label": "Sourced",
        "source_url": "https://docs.example.com/oauth",
        "quote": "Register an app without review",
    }
    data = {
        "app_name": "Example",
        "website": "example.com",
        "verdict": dict(sourced),
        "difficulty": "Easy",
        "hands_on_time": {"text": "5 to 15 minutes", "label": "Inferred"},
        "waiting_time": {"text": "None", "label": "Inferred"},
        "composio_status": {"text": "No toolkit found", "label": "Inferred"},
        "prerequisites": [dict(sourced)],
        "setup_steps": [dict(sourced)],
        "limits_before_approval": [dict(sourced)],
        "approval_process": [dict(sourced)],
        "likely_blockers": [dict(sourced)],
        "open_questions": [{"text": "Rate limits", "label": "Uncertain"}],
        "sources": [{"url": "https://docs.example.com/oauth"}],
        "last_verified": {"date": "2026-10-30", "by": "agent"},
        "meta": {"slug": "example"},
    }
    data.update(overrides)
    return data


def test_sourced_needs_url_and_quote():
    with pytest.raises(ValidationError, match="Sourced fact needs source_url and quote"):
        agent_fact(text="Approval takes two weeks", label=Label.SOURCED)
    with pytest.raises(ValidationError, match="needs quote"):
        agent_fact(text="x", label=Label.SOURCED, source_url="https://e.com/a")


def test_unsourced_labels_need_no_evidence():
    assert agent_fact(text="x", label=Label.INFERRED).source_url is None
    assert agent_fact(text="x", label=Label.UNCERTAIN).quote is None


def test_quote_word_limit():
    with pytest.raises(ValidationError, match="over the 25-word limit"):
        agent_fact(
            text="x",
            label=Label.SOURCED,
            source_url="https://e.com/a",
            quote=" ".join(["word"] * 26),
        )


def test_human_gold_is_exempt_from_url_and_quote():
    fact = Fact.model_validate(
        {"text": "x", "label": "Sourced"}, context={"provenance": "human-gold"}
    )
    assert fact.label is Label.SOURCED


@pytest.mark.parametrize("field", ["hands_on_time", "waiting_time"])
def test_time_is_never_tested(field):
    data = minimal_guide(**{field: {"text": "2 weeks", "label": "Tested"}})
    with pytest.raises(ValidationError, match="cannot be Tested"):
        Guide.model_validate(data)


def test_required_sections_must_be_present():
    with pytest.raises(ValidationError, match="these sections are empty"):
        Guide.model_validate(minimal_guide(setup_steps=[]))


def test_no_oauth_guides_may_omit_sections():
    data = minimal_guide(
        setup_steps=[],
        prerequisites=[],
        limits_before_approval=[],
        approval_process=[],
        likely_blockers=[],
        meta={"slug": "example", "no_oauth_found": True},
    )
    assert Guide.model_validate(data).meta.no_oauth_found


def test_cited_url_is_added_to_sources():
    data = minimal_guide(sources=[])
    guide = Guide.model_validate(data)
    assert [source.url for source in guide.sources] == ["https://docs.example.com/oauth"]


def test_gold_guide_loads_and_keeps_its_labels():
    guide = load_guide(GOLD)
    labels = [fact.label for _, _, fact in guide.iter_facts()]
    assert guide.app_name == "GitHub"
    assert guide.difficulty.value == "Easy"
    assert labels.count(Label.TESTED) == 10  # the ten hand-run setup steps
    assert len(guide.setup_steps) == 10
    assert guide.last_verified.by == "human"
    assert guide.meta.provenance == "human-gold"


def test_gold_time_estimate_was_downgraded():
    guide = load_guide(GOLD)
    assert guide.hands_on_time.label is Label.INFERRED
    assert "Tested only if you timed it" in guide.hands_on_time.note


@pytest.mark.parametrize(
    "raw,expected",
    [
        ("GitHub", "github"),
        ("Garmin Connect", "garmin-connect"),
        ("https://developer.spotify.com/documentation", "spotify"),
        ("www.quickbooks.com", "quickbooks"),
    ],
)
def test_slugify(raw, expected):
    assert slugify(raw) == expected
