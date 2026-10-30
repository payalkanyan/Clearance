"""Stage 5: a Sourced label survives only if its quote is really on the page."""

from __future__ import annotations

import pytest

from clearance import cache as cache_module
from clearance.cache import store_page
from clearance.citations import build_index, check, normalise, verify
from clearance.schema import Fact, Label

PAGE_URL = "https://docs.example.com/oauth"
OTHER_URL = "https://docs.example.com/scopes"

PAGE = (
    "# Create an app\n\n"
    "You must **register** an app before you can request tokens. "
    "Set the `redirect\\_uri` to your callback’s URL—see [the guide](/guide).\n\n"
    "A user or organization can own up to 100 OAuth apps.\n"
)
OTHER_PAGE = "Scopes are requested at authorization time, not in app settings.\n"


@pytest.fixture(autouse=True)
def index(tmp_path, monkeypatch):
    monkeypatch.setattr(cache_module, "CACHE_DIR", tmp_path / "cache")
    pages = [
        store_page("example", PAGE_URL, PAGE, source="firecrawl"),
        store_page("example", OTHER_URL, OTHER_PAGE, source="firecrawl"),
    ]
    return build_index("example", pages)


def sourced(quote: str, url: str = PAGE_URL) -> Fact:
    return Fact(text="a claim", label=Label.SOURCED, source_url=url, quote=quote)


def test_normalise_folds_formatting_not_wording():
    assert normalise("**bold**  text") == "bold text"
    assert normalise("redirect\\_uri") == "redirecturi"
    assert normalise("callback’s URL—here") == "callback's url-here"
    assert normalise("[the guide](/guide)") == "the guide"
    assert normalise("a b\n\nc") == "a b c"


def test_a_real_quote_verifies_through_markdown_noise(index):
    # The page writes this with bold, an escape, a curly quote and a dash.
    assert verify(sourced("You must register an app before you can request tokens."), index) is None
    assert verify(sourced("Set the redirect_uri to your callback's URL"), index) is None
    assert verify(sourced("A user or organization can own up to 100 OAuth apps."), index) is None


def test_a_paraphrase_is_caught(index):
    fact = sourced("You have to register an application before requesting tokens.")
    assert "does not appear in the cited page" in verify(fact, index)


def test_a_stitched_quote_is_named_as_such(index):
    fact = sourced(
        "You must register an app before you can request tokens and approval "
        "takes about two weeks in most cases"
    )
    reason = verify(fact, index)
    assert "first 8 words do" in reason
    assert "paraphrased or stitched" in reason


def test_quoting_the_wrong_page_is_caught(index):
    fact = sourced("Scopes are requested at authorization time", url=PAGE_URL)
    assert "does not appear in the cited page" in verify(fact, index)
    # ...and verifies when pointed at the page that actually says it.
    assert verify(sourced("Scopes are requested at authorization time", OTHER_URL), index) is None


def test_an_uncached_page_cannot_support_a_quote(index):
    fact = sourced("anything at all", url="https://docs.example.com/never-fetched")
    assert "never scraped" in verify(fact, index)


def test_url_differences_still_match(index):
    # A trailing slash and a fragment name the same page. A query string does
    # not, so it is deliberately not folded away.
    for variant in (PAGE_URL + "/", PAGE_URL + "#section"):
        fact = sourced("A user or organization can own up to 100 OAuth apps.", variant)
        assert verify(fact, index) is None, variant


@pytest.mark.parametrize(
    "quote,url,reason",
    [(None, PAGE_URL, "no quote"), ("x", None, "no source_url")],
)
def test_missing_evidence(quote, url, reason, index):
    # The schema rejects these for agent output; they only occur in a
    # human-written guide, where the citation rules are relaxed.
    fact = Fact.model_validate(
        {"text": "t", "label": "Sourced", "source_url": url, "quote": quote},
        context={"provenance": "human-gold"},
    )
    assert reason in verify(fact, index)


def test_check_downgrades_and_logs(index):
    good = sourced("A user or organization can own up to 100 OAuth apps.")
    bad = sourced("Approval usually takes two weeks.")
    inferred = Fact(text="untouched", label=Label.INFERRED)
    facts = [("prerequisites", 0, good), ("limits_before_approval", 1, bad),
             ("verdict", None, inferred)]

    result = check(facts, index, slug="example")

    assert result.checked == 2 and result.verified == 1
    assert len(result.downgrades) == 1
    assert result.ok is False
    assert good.label is Label.SOURCED
    assert bad.label is Label.INFERRED
    assert "downgraded from Sourced" in bad.note and result.at in bad.note
    assert inferred.label is Label.INFERRED and inferred.note is None
    downgrade = result.downgrades[0]
    assert downgrade.section == "limits_before_approval" and downgrade.index == 1
    assert downgrade.quote == "Approval usually takes two weeks."


def test_existing_notes_are_kept_when_downgrading(index):
    fact = sourced("not on the page")
    fact.note = "original note"
    check([("verdict", None, fact)], index, slug="example")
    assert fact.note.startswith("original note | downgraded from Sourced")
