"""Stage 3: what counts as an observation, and what must never become one."""

from __future__ import annotations

import pytest

from clearance import cache as cache_module
from clearance.cache import store_page
from clearance.probe import (
    Observation,
    ProbeResult,
    candidate_urls,
    classify,
    probe_facts,
)
from clearance.schema import Label

DOCS_URL = "https://docs.example.com/en/apps/creating-an-app"


@pytest.fixture(autouse=True)
def temp_cache(tmp_path, monkeypatch):
    monkeypatch.setattr(cache_module, "CACHE_DIR", tmp_path / "cache")
    yield


def seed(markdown: str, url: str = DOCS_URL, *, official: bool = True):
    page = store_page("example", url, markdown, source="firecrawl", official=official)
    return [page]


@pytest.mark.parametrize(
    "body,status,expected",
    [
        ("Sign in to continue\nPassword", 200, "login_wall"),
        ("", 401, "login_wall"),
        ("", 404, "not_found"),
        ("Contact sales to request API access", 200, "contact_sales"),
        ("This requires a paid plan. Upgrade your plan.", 200, "paid_plan_required"),
        (
            "Application name\nHomepage URL\nAuthorization callback URL\nDescription",
            200,
            "open_form",
        ),
        ("Marketing copy about our product", 200, "unclear"),
    ],
)
def test_classify(body, status, expected):
    observed, _, _ = classify(body, status)
    assert observed == expected


def test_a_screenshot_is_never_probed():
    pages = seed(
        "See [create app](https://assets.example.com/images/createappdialog.png) "
        "and [create app](https://www.example.com/images/create-app.png)"
    )
    assert candidate_urls("example", pages) == []


def test_documentation_pages_are_not_probed():
    # docs.example.com is where the form is described, not where it lives.
    pages = seed(
        "[app registration](https://docs.example.com/en/apps/modifying-a-registration) "
        "[create an app](https://docs.example.com/guides/apps/new)"
    )
    assert candidate_urls("example", pages) == []


def test_the_real_console_link_is_kept():
    pages = seed(
        "To register, go to "
        "[developer dashboard](https://www.example.com/settings/applications/new)"
    )
    candidates = candidate_urls("example", pages)
    assert [item["url"] for item in candidates] == [
        "https://www.example.com/settings/applications/new"
    ]


def test_links_to_other_sites_are_ignored():
    pages = seed("[create an app](https://someoneelse.com/apps/new)")
    assert candidate_urls("example", pages) == []


def test_already_scraped_pages_are_not_reprobed():
    pages = seed(f"[create an app]({DOCS_URL})")
    assert [item["url"] for item in candidate_urls("example", pages)] == []


def test_unofficial_pages_contribute_no_candidates():
    pages = seed(
        "[create an app](https://www.example.com/apps/new)",
        url="https://medium.com/@x/guide",
        official=False,
    )
    assert candidate_urls("example", pages) == []


def test_probe_facts_are_tested_and_carry_their_evidence():
    result = ProbeResult(
        slug="example",
        observations=[
            Observation(
                url="https://www.example.com/settings/applications/new",
                observed="login_wall",
                at="2026-10-30T10:00:00Z",
                status=200,
                signals=["sign in"],
            ),
            Observation(
                url="https://www.example.com/broken",
                observed="error",
                at="2026-10-30T10:00:01Z",
                error="HTTP 500",
            ),
        ],
    )
    facts = probe_facts(result)
    assert len(facts) == 1  # the failed load makes no claim
    fact = facts[0]
    assert fact.label is Label.TESTED
    assert fact.source_url == "https://www.example.com/settings/applications/new"
    assert "2026-10-30T10:00:00Z" in fact.note
    assert "sign in" in fact.note
