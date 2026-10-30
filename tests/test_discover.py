"""Stage 2 logic with a stubbed transport: no network, no credits."""

from __future__ import annotations

from types import SimpleNamespace

import pytest

from clearance import cache as cache_module
from clearance import discover as discover_module
from clearance.discover import discover
from clearance.fetch import FetchResult

OAUTH_PAGE = (
    "# Create an app\n\nRegister your app to get a client_id and client secret. "
    "Set the redirect uri to your callback.\n"
)
API_KEY_PAGE = "# Getting started\n\nPass your API key in the Authorization header.\n"


@pytest.fixture(autouse=True)
def temp_cache(tmp_path, monkeypatch):
    monkeypatch.setattr(cache_module, "CACHE_DIR", tmp_path / "cache")
    yield


def stub_search(results_by_query: dict[str, list[tuple[str, str]]] | list[tuple[str, str]]):
    def _search(query: str, per_query: int):
        results = (
            results_by_query
            if isinstance(results_by_query, list)
            else results_by_query.get(query, [])
        )
        return [
            SimpleNamespace(url=url, title=title, description=title)
            for url, title in results[:per_query]
        ]

    return _search


def stub_scrape(bodies: dict[str, str], *, status: dict[str, int] | None = None):
    calls: list[str] = []

    def _scrape(url: str):
        calls.append(url)
        code = (status or {}).get(url, 200)
        return (
            FetchResult(
                url=url,
                source="firecrawl",
                markdown=bodies.get(url, ""),
                status=code,
                title="stub",
            ),
            None,
        )

    return _scrape, calls


def test_official_pages_rank_above_blogs_and_blogs_are_marked(monkeypatch):
    official = "https://developer.spotify.com/documentation/web-api/concepts/apps"
    blog = "https://medium.com/@someone/spotify-oauth"
    monkeypatch.setattr(
        discover_module,
        "_search_once",
        stub_search([(official, "Apps | Spotify"), (blog, "Spotify OAuth guide")]),
    )
    scrape, _ = stub_scrape({official: OAUTH_PAGE, blog: OAUTH_PAGE})
    monkeypatch.setattr(discover_module, "scrape", scrape)

    result = discover("Spotify", use_cache=False)

    assert [page.url for page in result.pages][0] == official
    assert result.pages[0].official is True
    blog_page = next(page for page in result.pages if page.url == blog)
    assert blog_page.official is False
    assert result.no_oauth_found is False
    assert result.failed is None


def test_login_wall_is_recorded_as_a_gate_and_not_stored(monkeypatch):
    portal = "https://developer.example.com/apps/new"
    docs = "https://developer.example.com/docs/oauth"
    monkeypatch.setattr(
        discover_module,
        "_search_once",
        stub_search([(portal, "Create an app"), (docs, "OAuth")]),
    )
    scrape, calls = stub_scrape(
        {portal: "Sign in to continue", docs: OAUTH_PAGE}, status={portal: 200}
    )
    monkeypatch.setattr(discover_module, "scrape", scrape)

    result = discover("Example", use_cache=False)

    assert [gate.url for gate in result.gates] == [portal]
    assert portal not in [page.url for page in result.pages]
    assert calls.count(portal) == 1  # recorded, not retried
    assert result.gates[0].at.endswith("Z")


def test_api_key_only_app_reports_no_oauth(monkeypatch):
    url = "https://serpapi.com/search-api"
    monkeypatch.setattr(
        discover_module, "_search_once", stub_search([(url, "SerpApi search API")])
    )
    scrape, _ = stub_scrape({url: API_KEY_PAGE})
    monkeypatch.setattr(discover_module, "scrape", scrape)

    result = discover("SerpApi", use_cache=False)

    assert result.no_oauth_found is True
    assert result.failed is None


def test_failed_search_is_not_reported_as_no_oauth(monkeypatch):
    def boom(query: str, per_query: int):
        raise RuntimeError("Website Not Supported: proxy detected")

    monkeypatch.setattr(discover_module, "_search_once", boom)
    monkeypatch.setattr(discover_module, "firecrawl_degraded", lambda: True)

    result = discover("Spotify", use_cache=False)

    assert result.no_oauth_found is False
    assert "every search query failed" in result.failed
    assert result.pages == []


def test_second_run_serves_pages_from_cache(monkeypatch):
    url = "https://developer.example.com/docs/oauth"
    monkeypatch.setattr(
        discover_module, "_search_once", stub_search([(url, "OAuth")])
    )
    scrape, calls = stub_scrape({url: OAUTH_PAGE})
    monkeypatch.setattr(discover_module, "scrape", scrape)

    first = discover("Example", use_cache=False)
    assert first.from_cache is False

    second = discover("Example", use_cache=True)
    assert second.from_cache is True
    assert [page.url for page in second.pages] == [url]
    assert len(calls) == 1  # nothing re-fetched


def test_cached_page_text_is_what_was_fetched(monkeypatch):
    url = "https://developer.example.com/docs/oauth"
    monkeypatch.setattr(discover_module, "_search_once", stub_search([(url, "OAuth")]))
    scrape, _ = stub_scrape({url: OAUTH_PAGE})
    monkeypatch.setattr(discover_module, "scrape", scrape)

    result = discover("Example", use_cache=False)
    texts = cache_module.pages_text(result.slug, result.pages)
    assert texts[url] == OAUTH_PAGE
