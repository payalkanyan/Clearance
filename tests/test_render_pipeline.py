"""The markdown rendering and the pieces of the pipeline worth isolating."""

from __future__ import annotations

import json

import pytest

from clearance import pipeline as pipeline_module
from clearance.discover import DiscoveryResult
from clearance.pipeline import (
    FACT_SECTIONS,
    PROBE_PLACEMENT,
    guide_paths,
    no_oauth_guide,
    strip_scheme,
)
from clearance.probe import DESCRIPTIONS
from clearance.render import render
from clearance.schema import (
    Difficulty,
    Fact,
    Guide,
    Label,
    Meta,
    Source,
    Verified,
    load_guide,
)


def guide() -> Guide:
    sourced = Fact(
        text="You need an account",
        label=Label.SOURCED,
        source_url="https://docs.example.com/oauth",
        quote="You need an account",
    )
    return Guide(
        app_name="Example",
        website="example.com/console",
        verdict=Fact(text="Self-serve", label=Label.INFERRED),
        difficulty=Difficulty.MEDIUM,
        difficulty_reason=Fact(text="A user cap applies", label=Label.SOURCED,
                               source_url="https://docs.example.com/oauth",
                               quote="up to 25 users"),
        hands_on_time=Fact(text="5 to 15 minutes", label=Label.INFERRED),
        waiting_time=Fact(text="2 to 6 weeks", label=Label.UNCERTAIN),
        composio_status=Fact(text="Managed OAuth app", label=Label.INFERRED),
        prerequisites=[sourced],
        setup_steps=[Fact(text="Open the console", label=Label.TESTED,
                          source_url="https://example.com/console",
                          note="observed at 2026-10-30T10:00:00Z")],
        scopes=[Fact(text="read:user", label=Label.INFERRED)],
        limits_before_approval=[sourced],
        approval_process=[sourced],
        likely_blockers=[sourced],
        agent_can_do=["Read the docs"],
        you_must_do=["Click Allow"],
        open_questions=[Fact(text="Rate limits?", label=Label.UNCERTAIN)],
        sources=[Source(url="https://docs.example.com/oauth", title="OAuth")],
        last_verified=Verified(date="2026-10-30", by="agent"),
        meta=Meta(slug="example", model="gemini-3.8-flash"),
    )


def test_render_shows_every_section_and_label():
    text = render(guide())
    for heading in ("Prerequisites", "Setup steps", "Scopes", "Limits before approval",
                    "Approval process", "Likely blockers", "Agent can do",
                    "You must do", "Open questions", "Sources"):
        assert f"**{heading}**" in text
    for label in ("Sourced", "Inferred", "Uncertain", "Tested"):
        assert f"*({label})*" in text
    assert "**Example, example.com/console**" in text
    assert "**Difficulty:** Medium" in text
    assert "**Last verified:** 2026-10-30, by agent." in text


def test_render_shows_the_quote_and_its_source():
    text = render(guide())
    assert '> "You need an account" — [source](https://docs.example.com/oauth)' in text
    # A Tested fact has no quote, so its note carries the evidence.
    assert "> observed at 2026-10-30T10:00:00Z" in text


def test_render_numbers_the_setup_steps():
    assert "1. Open the console" in render(guide())


def test_the_gold_guide_renders():
    text = render(load_guide("guides/github.json"))
    assert text.startswith("# GitHub")
    assert "*(Tested)*" in text  # the ten hand-run steps survive


@pytest.mark.parametrize(
    "url,expected",
    [("https://example.com/a/", "example.com/a"), ("example.com", "example.com"), (None, "")],
)
def test_strip_scheme(url, expected):
    assert strip_scheme(url) == expected


def test_a_human_gold_guide_is_never_overwritten(tmp_path, monkeypatch):
    monkeypatch.setattr(pipeline_module, "GUIDES_DIR", tmp_path)
    (tmp_path / "github.json").write_text(
        json.dumps({"meta": {"slug": "github", "provenance": "human-gold"}})
    )
    assert guide_paths("github") == ("github.agent.json", "github.agent.md")

    (tmp_path / "spotify.json").write_text(
        json.dumps({"meta": {"slug": "spotify", "provenance": "agent"}})
    )
    assert guide_paths("spotify") == ("spotify.json", "spotify.md")
    assert guide_paths("never-seen") == ("never-seen.json", "never-seen.md")


def test_no_oauth_guide_is_honest_rather_than_easy():
    discovery = DiscoveryResult(
        slug="serpapi",
        app_name="SerpApi",
        website="https://serpapi.com/search-api",
        queries=[{"query": "SerpApi OAuth app registration", "results": 3}],
        no_oauth_found=True,
    )
    built = no_oauth_guide(
        discovery, Fact(text="No toolkit", label=Label.INFERRED), "gemini-3.8-flash"
    )
    assert built.difficulty is Difficulty.UNKNOWN  # not Easy
    assert built.meta.no_oauth_found is True
    assert built.setup_steps == []  # no invented steps
    assert "No OAuth app found" in built.verdict.text
    assert built.verdict.label is Label.INFERRED
    assert render(built).startswith("# SerpApi")


def test_every_probe_outcome_has_a_place_in_the_guide():
    outcomes = set(DESCRIPTIONS) - {"error"}  # a failed load makes no claim
    assert outcomes <= set(PROBE_PLACEMENT)
    assert set(PROBE_PLACEMENT.values()) <= set(FACT_SECTIONS)
