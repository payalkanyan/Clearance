"""Stage 6b: what Composio's own page says, quoted accurately or not at all."""

from __future__ import annotations

from clearance.composio import (
    ComposioStatus,
    build_fact,
    candidate_slugs,
    classify,
    find_quote,
)
from clearance.schema import Label

MANAGED = (
    "Load more FAQ ## Frequently asked questions ### Do I need my own GitHub "
    "developer credentials or OAuth app?+ No. Composio provides a managed OAuth "
    "app for GitHub, so you sign in with your normal GitHub account and approve "
    "access. If you later want your own name on the consent screen, you can add "
    "your own GitHub OAuth app in the Composio dashboard."
)
BYO = (
    "captioning from one API.](https://composio.dev/toolkits/captions) Load more "
    "FAQ ## Frequently asked questions ### Do I need my own Spotify developer "
    "credentials or OAuth app?+ Spotify requires connections to go through your "
    "own OAuth app. You register it once with Spotify."
)
API_KEY = "### How do I connect?+ Amara uses an API key to connect. Paste it in."


def test_managed_is_detected_and_quoted():
    kind, quote = classify(MANAGED)
    assert kind == "managed"
    assert quote == (
        "Composio provides a managed OAuth app for GitHub, so you sign in with "
        "your normal GitHub account and approve access."
    )


def test_managed_wins_over_the_optional_bring_your_own_sentence():
    # The same page also says you *can* add your own app. That is not the answer.
    assert classify(MANAGED)[0] == "managed"


def test_bring_your_own_quote_skips_the_link_debris_before_it():
    kind, quote = classify(BYO)
    assert kind == "bring-your-own"
    assert quote == "Spotify requires connections to go through your own OAuth app."
    assert "](" not in quote and "http" not in quote


def test_api_key_toolkit():
    assert classify(API_KEY)[0] == "toolkit-no-oauth"


def test_a_page_that_says_nothing():
    assert classify("Spotify is a streaming service. 84 Tools3 Triggers") == ("unknown", None)


def test_quote_must_be_verbatim_or_it_is_dropped():
    # find_quote collapses whitespace, which stage 5 also does, so this holds.
    quote = find_quote(MANAGED, (r"provides a managed OAuth app",))
    assert quote in " ".join(MANAGED.split())


def test_candidate_slugs():
    assert candidate_slugs("Garmin Connect") == ["garmin-connect", "garminconnect", "garmin"]
    assert candidate_slugs("GitHub") == ["github"]


def test_fact_is_sourced_only_with_a_quote():
    with_quote = build_fact(
        ComposioStatus(slug="github", kind="managed", url="https://composio.dev/toolkits/github",
                       quote="Composio provides a managed OAuth app for GitHub.")
    )
    assert with_quote.label is Label.SOURCED
    assert with_quote.quote and with_quote.source_url

    without_quote = build_fact(
        ComposioStatus(slug="x", kind="managed", url="https://composio.dev/toolkits/x")
    )
    assert without_quote.label is Label.INFERRED
    assert "quoted cleanly" in without_quote.note


def test_no_toolkit_is_inferred_and_names_what_was_tried():
    fact = build_fact(
        ComposioStatus(
            slug="garmin-connect",
            kind="none",
            tried=[{"url": "https://composio.dev/toolkits/garmin", "status": 404}],
        )
    )
    assert fact.label is Label.INFERRED
    assert "garmin" in fact.note
    assert "different slug" in fact.note
