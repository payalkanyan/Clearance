"""Stage 2: find the provider's official OAuth pages and scrape them.

Six fixed queries per app, so a run is reproducible and the log shows exactly
what was asked. Ranking is plain code: official-looking hosts first, then path
keywords. Community sites are kept but marked unofficial, because guide-spec
section 2 says a blog or forum can support Inferred at best, never Sourced.
"""

from __future__ import annotations

import re
from typing import Callable
from urllib.parse import urlsplit

from pydantic import BaseModel

from .cache import (
    PageRecord,
    load_pages,
    normalise_url,
    read_json,
    save_pages,
    slug_dir,
    store_page,
    write_json,
)
from .config import slugify, utc_now
from .fetch import (
    FetchResult,
    firecrawl_client,
    firecrawl_degraded,
    looks_like_gate,
    note_key_rejected,
    scrape,
)

QUERY_TEMPLATES = (
    "{app} OAuth app registration",
    "{app} developer console create app",
    "{app} API scopes permissions",
    "{app} app review verification process",
    "{app} production access quota extension",
    "{app} developer terms of service",
)

# Hosts that can never carry a Sourced fact.
COMMUNITY_HOSTS = (
    "medium.com",
    "dev.to",
    "stackoverflow.com",
    "stackexchange.com",
    "reddit.com",
    "quora.com",
    "hashnode.dev",
    "substack.com",
    "youtube.com",
    "linkedin.com",
    "twitter.com",
    "x.com",
    "facebook.com",
    "blogspot.com",
    "wordpress.com",
    "wikipedia.org",
    "gist.github.com",
    "npmjs.com",
    "pypi.org",
    "zapier.com",
    "make.com",
    "n8n.io",
    "pipedream.com",
)

HOST_PREFIXES = ("www", "developer", "developers", "docs", "dev", "api", "platform",
                 "console", "support", "help", "cloud", "portal")

# A provider's own forum is still a forum: user posts, not documentation.
FORUM_HOST_PREFIXES = ("community", "forum", "forums", "answers", "discuss",
                       "discussions", "ask")
FORUM_PATH_MARKERS = ("/forum/", "/forums/", "/discussion/", "/discussions/",
                      "/community/", "/questions/", "/thread/", "/topic/")

# Where a provider puts the pages we actually want.
DOCS_HOST_PREFIXES = ("developer", "developers", "docs", "platform", "api")

TLD_PARTS = {"com", "org", "net", "io", "dev", "co", "uk", "ai", "app", "me", "us",
             "gov", "edu", "info", "cloud", "tech", "online", "site"}

PATH_KEYWORDS = {
    "oauth": 5, "authoriz": 4, "register": 4, "registration": 4, "scope": 4,
    "review": 3, "verif": 3, "approval": 3, "permission": 3, "credential": 3,
    "production": 2, "quota": 2, "rate-limit": 2, "app": 2, "application": 2,
    "developer": 2, "auth": 2, "token": 1, "api": 1, "terms": 1, "policy": 1,
    "getting-started": 1, "quickstart": 1,
}

# A page must show one of these to count as documenting an OAuth flow.
OAUTH_MARKERS = (
    "oauth",
    "client_id",
    "client id",
    "client secret",
    "redirect uri",
    "redirect_uri",
    "authorization code",
)

DEFAULT_PAGE_LIMIT = 7

# Once this many official pages are in hand, stop spending on third-party ones.
MIN_OFFICIAL_BEFORE_SKIPPING = 3


class Candidate(BaseModel):
    url: str
    title: str | None = None
    description: str | None = None
    query: str | None = None
    position: int | None = None
    score: float = 0.0
    official: bool = True
    reasons: list[str] = []


class Gate(BaseModel):
    url: str
    reason: str
    status: int | None = None
    at: str


class DiscoveryResult(BaseModel):
    slug: str
    app_name: str
    website: str | None = None
    queries: list[dict] = []
    candidates: list[Candidate] = []
    pages: list[PageRecord] = []
    gates: list[Gate] = []
    fallbacks: list[dict] = []
    skipped: list[dict] = []
    no_oauth_found: bool = False
    failed: str | None = None
    from_cache: bool = False
    fetch_usage: list[dict] = []


def host_tokens(url: str) -> set[str]:
    """developer.intuit.com -> {'intuit'}; quickbooks.intuit.com -> both labels."""
    labels = [part for part in urlsplit(url).netloc.lower().split(".") if part]
    while labels and labels[0] in HOST_PREFIXES:
        labels.pop(0)
    while labels and labels[-1] in TLD_PARTS:
        labels.pop()
    return set(labels)


def is_community(url: str) -> bool:
    parts = urlsplit(url)
    host = parts.netloc.lower()
    if any(host == bad or host.endswith("." + bad) for bad in COMMUNITY_HOSTS):
        return True
    if host.split(".")[0] in FORUM_HOST_PREFIXES:
        return True
    path = parts.path.lower()
    return any(marker in path for marker in FORUM_PATH_MARKERS)


def app_tokens(app_name: str) -> set[str]:
    return {token for token in slugify(app_name).split("-") if len(token) > 2}


def score_candidate(
    candidate: Candidate, tokens: set[str], frequent_hosts: set[str]
) -> Candidate:
    reasons: list[str] = []
    score = 0.0
    host = urlsplit(candidate.url).netloc.lower()
    text = f"{candidate.title or ''} {candidate.description or ''}".lower()

    if is_community(candidate.url):
        candidate.official = False
        score -= 8
        reasons.append("third-party host")
    else:
        if tokens & host_tokens(candidate.url):
            score += 6
            reasons.append("host matches the app name")
        elif host in frequent_hosts:
            score += 4
            reasons.append("host dominates the search results")
        elif any(token in text for token in tokens):
            score += 2
            reasons.append("app named in the result")
        else:
            candidate.official = False
            reasons.append("cannot confirm this is the provider")

    if host.split(".")[0] in DOCS_HOST_PREFIXES:
        score += 2
        reasons.append("developer documentation host")

    path = urlsplit(candidate.url).path.lower()
    for keyword, weight in PATH_KEYWORDS.items():
        if keyword in path:
            score += weight
    if candidate.position:
        score += max(0, 3 - candidate.position * 0.3)

    candidate.score = round(score, 2)
    candidate.reasons = reasons
    return candidate


def _search_once(query: str, per_query: int):
    data = firecrawl_client().search(
        query, limit=per_query, sources=["web"], domain_tools=False
    )
    return list(data.web or [])


def search(app_name: str, *, per_query: int = 5) -> tuple[list[Candidate], list[dict]]:
    client = firecrawl_client()
    candidates: dict[str, Candidate] = {}
    log: list[dict] = []
    for template in QUERY_TEMPLATES:
        query = template.format(app=app_name)
        try:
            results = _search_once(query, per_query)
        except Exception as exc:
            if ("unauthorized" in str(exc).lower() or "invalid token" in str(exc).lower()) \
                    and not firecrawl_degraded():
                note_key_rejected()  # fall back to the keyless free tier
                client = firecrawl_client()
                try:
                    results = _search_once(query, per_query)
                except Exception as retry_exc:
                    log.append({"query": query, "error": str(retry_exc)[:200]})
                    continue
            else:
                log.append({"query": query, "error": str(exc)[:200]})
                continue
        urls: list[str] = []
        for position, item in enumerate(results, start=1):
            url = normalise_url(getattr(item, "url", "") or "")
            if not url:
                continue
            urls.append(url)
            if url not in candidates:
                candidates[url] = Candidate(
                    url=url,
                    title=getattr(item, "title", None),
                    description=getattr(item, "description", None),
                    query=query,
                    position=position,
                )
        log.append({"query": query, "results": len(results), "urls": urls})
    return list(candidates.values()), log


def rank(candidates: list[Candidate], app_name: str) -> list[Candidate]:
    tokens = app_tokens(app_name)
    counts: dict[str, int] = {}
    for candidate in candidates:
        if not is_community(candidate.url):
            host = urlsplit(candidate.url).netloc.lower()
            counts[host] = counts.get(host, 0) + 1
    frequent = {host for host, count in counts.items() if count >= 3}
    scored = [score_candidate(candidate, tokens, frequent) for candidate in candidates]
    return sorted(scored, key=lambda item: item.score, reverse=True)


def has_oauth_evidence(slug: str, pages: list[PageRecord]) -> bool:
    from .cache import page_text

    for page in pages:
        if not page.official:
            continue
        body = page_text(slug, page).lower()
        if any(marker in body for marker in OAUTH_MARKERS):
            return True
    return False


def discover(
    app_input: str,
    *,
    limit: int = DEFAULT_PAGE_LIMIT,
    use_cache: bool = True,
    progress: Callable[[str, str], None] | None = None,
) -> DiscoveryResult:
    def emit(message: str) -> None:
        if progress:
            progress("discover", message)

    slug = slugify(app_input)
    is_url = bool(re.match(r"^[a-z][a-z0-9+.-]*://", app_input, re.I))
    app_name = slug.replace("-", " ").title() if is_url else app_input.strip()
    result = DiscoveryResult(slug=slug, app_name=app_name)

    cached_pages = load_pages(slug) if use_cache else []
    if cached_pages:
        emit(f"cache hit: {len(cached_pages)} pages already scraped")
        cached = read_json(slug_dir(slug) / "discovery.json", default={}) or {}
        result = DiscoveryResult.model_validate(
            {**cached, "slug": slug, "app_name": cached.get("app_name", app_name),
             "pages": [page.model_dump() for page in cached_pages], "from_cache": True}
        )
        return result

    emit(f"searching: {len(QUERY_TEMPLATES)} queries")
    candidates, result.queries = search(app_name)
    if is_url:  # the user handed us a page; trust it
        seeded = Candidate(url=normalise_url(app_input), query="user input", position=1)
        candidates.insert(0, seeded)
    result.candidates = rank(candidates, app_name)
    emit(f"ranked {len(result.candidates)} candidate pages")

    pages: list[PageRecord] = []
    for candidate in result.candidates:
        official_so_far = sum(1 for page in pages if page.official)
        if not candidate.official and official_so_far >= MIN_OFFICIAL_BEFORE_SKIPPING:
            result.skipped.append(
                {"url": candidate.url, "reason": "unofficial, official pages suffice"}
            )
            continue
        if len(pages) >= limit:
            result.skipped.append({"url": candidate.url, "reason": "page limit reached"})
            continue
        if candidate.score <= 0:
            result.skipped.append({"url": candidate.url, "reason": "low score"})
            continue
        emit(f"scraping {candidate.url}")
        fetched, first_attempt = scrape(candidate.url)
        if first_attempt is not None:
            result.fallbacks.append(
                {
                    "url": candidate.url,
                    "firecrawl_error": first_attempt.error,
                    "kind": first_attempt.error_kind,
                    "fallback_ok": fetched.ok,
                }
            )
            emit(f"firecrawl {first_attempt.error_kind}; used web_fetch")
        if fetched.usage:
            result.fetch_usage.append(fetched.usage)

        gate = looks_like_gate(fetched)
        if gate:
            result.gates.append(
                Gate(url=candidate.url, reason=gate, status=fetched.status, at=utc_now())
            )
            emit(f"gate at {candidate.url}: {gate}")
            continue  # recorded, not retried
        if not fetched.ok:
            result.skipped.append(
                {"url": candidate.url, "reason": fetched.error or "fetch failed"}
            )
            continue
        pages.append(
            store_page(
                slug,
                candidate.url,
                fetched.markdown or "",
                source=fetched.source,
                title=fetched.title or candidate.title,
                status=fetched.status,
                official=candidate.official,
                query=candidate.query,
            )
        )

    result.pages = pages
    result.website = urlsplit(pages[0].url).netloc if pages else None

    official = [page for page in pages if page.official]
    if not official:
        # No official page was read, so we know nothing about this app either
        # way. Saying "no OAuth" here would be inventing a finding.
        errors = [item["error"] for item in result.queries if item.get("error")]
        if errors:
            result.failed = f"every search query failed: {errors[0]}"
        elif not result.candidates:
            result.failed = "search returned no candidate pages"
        else:
            result.failed = "no official page could be read"
        emit(f"discovery failed: {result.failed}")
    else:
        result.no_oauth_found = not has_oauth_evidence(slug, official)
        if result.no_oauth_found:
            emit("no OAuth evidence on any official page")

    if result.failed:
        emit("nothing cached: a failed run must not look like a result")
        return result

    save_pages(slug, pages)
    write_json(
        slug_dir(slug) / "discovery.json",
        result.model_dump(exclude={"pages", "from_cache"}),
    )
    emit(f"kept {len(pages)} pages, {len(result.gates)} gates")
    return result


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Stage 2: discover and scrape.")
    parser.add_argument("app", help="app name or website")
    parser.add_argument("--limit", type=int, default=DEFAULT_PAGE_LIMIT)
    parser.add_argument("--no-cache", action="store_true")
    args = parser.parse_args(argv)

    result = discover(
        args.app,
        limit=args.limit,
        use_cache=not args.no_cache,
        progress=lambda stage, message: print(f"  [{stage}] {message}"),
    )

    print(f"\n{result.app_name} ({result.slug})"
          f"{' - from cache' if result.from_cache else ''}")
    print(f"  pages: {len(result.pages)}  gates: {len(result.gates)}  "
          f"fallbacks: {len(result.fallbacks)}  no_oauth_found: {result.no_oauth_found}")
    if result.failed:
        print(f"  FAILED: {result.failed}")
        print("  (check FIRECRAWL_API_KEY in .env; keyless use is blocked from "
              "VPN and proxy networks)")
    for page in result.pages:
        flag = "" if page.official else "  [unofficial: Inferred at best]"
        print(f"   - {page.url}  ({page.bytes} B via {page.source}){flag}")
    for gate in result.gates:
        print(f"   ! gate {gate.url}: {gate.reason}")
    for item in result.skipped[:5]:
        print(f"   x skipped {item['url']}: {item['reason']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
