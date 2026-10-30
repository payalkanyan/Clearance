"""Stage 4 without the API: the schema guarantee, the budget, the repairs."""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from clearance import cache as cache_module
from clearance.cache import store_page
from clearance.extract import (
    DraftFact,
    GuideDraft,
    ProbeResult,
    build_pages_block,
    repair,
    shorten_quote,
    website_for,
)
from clearance.probe import Observation

CITABLE = ["https://docs.example.com/oauth"]


@pytest.fixture(autouse=True)
def temp_cache(tmp_path, monkeypatch):
    monkeypatch.setattr(cache_module, "CACHE_DIR", tmp_path / "cache")
    yield


def draft(**overrides) -> GuideDraft:
    base = {
        "app_name": "Example",
        "website": "example.com",
        "verdict": {"text": "Self-serve", "label": "Inferred"},
        "hands_on_time": {"text": "5 to 15 minutes", "label": "Inferred"},
        "waiting_time": {"text": "None", "label": "Inferred"},
        "prerequisites": [],
        "setup_steps": [],
        "scopes": [],
        "limits_before_approval": [],
        "approval_process": [],
        "likely_blockers": [],
        "agent_can_do": [],
        "you_must_do": [],
        "open_questions": [],
    }
    base.update(overrides)
    return GuideDraft.model_validate(base)


def test_the_model_cannot_emit_tested():
    """The draft enum has no Tested member, so the label is unreachable by the
    model rather than merely discouraged by the prompt."""
    with pytest.raises(ValidationError):
        DraftFact(text="I saw the form", label="Tested")
    assert "Tested" not in str(GuideDraft.model_json_schema())


@pytest.mark.parametrize(
    "fact,reason",
    [
        ({"text": "x", "label": "Sourced"}, "no source_url"),
        ({"text": "x", "label": "Sourced", "source_url": CITABLE[0]}, "no quote"),
        (
            {
                "text": "x",
                "label": "Sourced",
                "source_url": "https://blog.example.com/post",
                "quote": "something",
            },
            "not one of the official pages",
        ),
    ],
)
def test_unsupported_sourced_facts_are_downgraded(fact, reason):
    fixed, repairs = repair(draft(prerequisites=[fact]), CITABLE)
    assert fixed.prerequisites[0].label == "Inferred"
    assert reason in repairs[0]
    assert "downgraded from Sourced" in fixed.prerequisites[0].note


def test_a_good_sourced_fact_is_left_alone():
    fact = {
        "text": "You need an account",
        "label": "Sourced",
        "source_url": CITABLE[0],
        "quote": "You need an account",
    }
    fixed, repairs = repair(draft(prerequisites=[fact]), CITABLE)
    assert fixed.prerequisites[0].label == "Sourced"
    assert repairs == []


def test_over_long_quote_is_trimmed_not_dropped():
    quote = " ".join(["word"] * 40)
    fact = {"text": "x", "label": "Sourced", "source_url": CITABLE[0], "quote": quote}
    fixed, repairs = repair(draft(setup_steps=[fact]), CITABLE)
    assert fixed.setup_steps[0].label == "Sourced"
    assert len(fixed.setup_steps[0].quote.split()) <= 24
    assert quote.startswith(fixed.setup_steps[0].quote)  # still verbatim
    assert "trimmed" in repairs[0]


def test_empty_facts_are_dropped_and_singles_get_a_placeholder():
    fixed, repairs = repair(
        draft(
            prerequisites=[{"text": "   ", "label": "Inferred"}],
            verdict={"text": "", "label": "Inferred"},
        ),
        CITABLE,
    )
    assert fixed.prerequisites == []
    assert fixed.verdict.label == "Uncertain"
    assert any("empty text" in item for item in repairs)


def test_shorten_quote_prefers_a_sentence_end():
    quote = "Users can edit their scopes after the flow. " + " ".join(["filler"] * 30)
    assert shorten_quote(quote) == "Users can edit their scopes after the flow."

    # Nothing to cut at: fall back to a word boundary.
    assert shorten_quote(" ".join(["a"] * 40)) == " ".join(["a"] * 24)

    # A quote already inside the limit comes back untouched.
    short = "You need an account."
    assert shorten_quote(short) == short


def test_pages_are_capped_and_third_party_pages_are_not_citable():
    official = store_page(
        "example", "https://docs.example.com/oauth", "A" * 50_000, source="firecrawl"
    )
    blog = store_page(
        "example",
        "https://medium.com/@x/guide",
        "B" * 100,
        source="firecrawl",
        official=False,
    )
    block, trimmed, citable = build_pages_block("example", [official, blog])

    assert citable == ["https://docs.example.com/oauth"]
    assert trimmed[0]["kept_chars"] == 40_000
    assert trimmed[0]["original_chars"] == 50_000
    assert "THIRD-PARTY (Inferred at best)" in block
    assert "A" * 40_000 in block and "A" * 40_001 not in block


def test_website_prefers_the_probed_console():
    page = store_page(
        "example", "https://docs.example.com/oauth", "x", source="firecrawl"
    )
    probe = ProbeResult(
        slug="example",
        observations=[
            Observation(
                url="https://www.example.com/settings/apps/new",
                observed="login_wall",
                at="2026-10-30T10:00:00Z",
            )
        ],
    )
    assert website_for([page], probe) == "www.example.com/settings/apps/new"
    assert website_for([page], None) == "docs.example.com"
