"""Stage 3: visit the app-creation page and record what is actually there.

These are the only facts in a guide labelled Tested, and they are written here
in code, never by the model: the agent really did open the URL and see this.
Each one carries the URL, the HTTP status and a UTC timestamp.
"""

from __future__ import annotations

import re
from typing import Callable
from urllib.parse import urljoin, urlsplit

from pydantic import BaseModel

from .cache import load_pages, normalise_url, page_text, read_json, slug_dir, write_json
from .composio import COMPOSIO_HOSTS
from .config import slugify, utc_now
from .fetch import scrape
from .schema import Fact, Label

# Paths that are usually where you register an app.
PATH_HINTS = (
    "/apps/new", "/applications/new", "/app/new", "/new-app", "/create-app",
    "/apps/create", "/oauth/applications", "/settings/developers",
    "/settings/applications", "/my-apps", "/dashboard", "/developer/register",
    "/register", "/signup", "/sign-up", "/create", "/apps", "/console",
    # Intuit and others put the portal under /app/developer rather than /apps.
    "/app/developer", "/developer/homepage", "/developer/dashboard",
)

# Link text that points at the same thing.
LABEL_HINTS = (
    "create an app", "create app", "new app", "register an app", "register app",
    "my apps", "developer dashboard", "dashboard", "app registration",
    "create a client", "register your application", "developer portal",
    "sign up", "get started", "request access", "developer homepage",
    "developer home", "developer console",
)

LOGIN_MARKERS = (
    "sign in", "signin", "log in", "login", "password", "continue with google",
    "continue with apple", "sign in to continue", "create an account",
    "forgot password", "two-factor",
)
PAID_MARKERS = (
    "upgrade your plan", "paid plan", "requires a paid", "subscription required",
    "upgrade to", "premium plan", "enterprise plan", "billing required",
    "start your free trial",
)
SALES_MARKERS = (
    "contact sales", "talk to sales", "contact our sales", "book a demo",
    "request a demo", "request access", "apply for access", "get in touch",
    "contact us to get started", "partner application",
)
NOT_FOUND_MARKERS = ("page not found", "404", "we couldn't find", "does not exist")

# Field labels a registration form tends to show.
FORM_FIELDS = (
    "app name", "application name", "client name", "redirect uri", "redirect url",
    "callback url", "callback uri", "homepage url", "website url", "website",
    "description", "company", "organization", "organisation", "email", "scopes",
    "privacy policy", "terms of service", "logo", "app type", "application type",
    "platform", "webhook", "contact email", "app icon",
)

MARKDOWN_LINK = re.compile(r"\[([^\]]{0,120})\]\((https?://[^\s)]+|/[^\s)]*)\)")

# A screenshot of a form is not a form. Docs are full of them, and scraping one
# would manufacture a Tested fact about a page nobody opened.
SKIP_EXTENSIONS = (
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".avif", ".ico", ".pdf",
    ".zip", ".tar", ".gz", ".mp4", ".mov", ".webm", ".mp3", ".css", ".js",
    ".json", ".xml", ".txt", ".yaml", ".yml",
)
ASSET_HOST_MARKERS = ("cdn", "assets", "static", "images", "img", "media", "files")

# Documentation about registering an app is not the registration page. A docs
# page listing the dialog's fields would otherwise read as an open form.
DEMOTE_PATH_MARKERS = (
    "/reference/", "/api-reference/", "/changelog", "/blog/", "/documentation/",
    "/docs/", "/tutorials/", "/concepts/", "/guides/", "/learn/", "/faq",
)

# Hosts that serve documentation. You register an app on a console, not here,
# and a docs page listing a dialog's fields otherwise reads as an open form.
DOCS_HOST_LABELS = ("docs", "help", "support", "learn", "guides", "knowledge")

# Below this, a link is not plausibly an app-creation page.
MIN_CANDIDATE_SCORE = 4

TEXT_CONTENT = ("html", "text", "xml")

DEFAULT_PROBE_LIMIT = 2


class Observation(BaseModel):
    url: str
    observed: str  # login_wall | contact_sales | paid_plan_required |
                   # application_form | open_form | not_found | error | unclear
    at: str
    status: int | None = None
    source: str | None = None
    signals: list[str] = []
    fields_visible: list[str] = []
    bytes: int = 0
    error: str | None = None
    why: str | None = None  # how this URL was chosen


class ProbeResult(BaseModel):
    slug: str
    observations: list[Observation] = []
    considered: list[dict] = []
    from_cache: bool = False


def links_in(markdown: str, base_url: str) -> list[tuple[str, str]]:
    """(url, link text) pairs from a cached page, made absolute."""
    found: list[tuple[str, str]] = []
    for label, target in MARKDOWN_LINK.findall(markdown):
        url = urljoin(base_url, target)
        if url.startswith("http"):
            found.append((normalise_url(url), label.strip().lower()))
    return found


def candidate_urls(slug: str, pages=None) -> list[dict]:
    """Rank links from the cached pages by how much they look like a signup page."""
    pages = pages if pages is not None else load_pages(slug)
    # Composio's pages are evidence about Composio. The console we want to see
    # belongs to the provider.
    def is_composio(url: str) -> bool:
        host = urlsplit(url).netloc.lower()
        return any(host == name or host.endswith("." + name) for name in COMPOSIO_HOSTS)

    # The kind field covers pages cached from now on; the host check covers any
    # pages.json written before that field existed.
    provider_pages = [
        page for page in pages
        if page.kind != "composio" and not is_composio(page.url)
    ]
    provider_hosts = {
        urlsplit(page.url).netloc.lower() for page in provider_pages if page.official
    }
    roots = {host.split(".")[-2] for host in provider_hosts if "." in host}

    already_read = {normalise_url(page.url) for page in pages}

    scored: dict[str, dict] = {}
    # A third-party page may name the real console URL. Taking the URL from it is
    # safe: it has to be on the provider's own host, and what we then record is
    # what the agent sees there, not what the page claimed.
    for page in provider_pages:
        for url, label in links_in(page_text(slug, page), page.url):
            host = urlsplit(url).netloc.lower()
            # Stay on the provider: a signup page is never on someone else's site.
            if not (host in provider_hosts or any(root in host for root in roots)):
                continue
            if url in already_read:
                continue  # already scraped as documentation in stage 2
            if is_composio(url):
                continue
            first_label = host.split(".")[0]
            if any(marker in first_label for marker in ASSET_HOST_MARKERS):
                continue
            path = urlsplit(url).path.lower()
            if path.endswith(SKIP_EXTENSIONS):
                continue
            score = 0
            why: list[str] = []
            for hint in PATH_HINTS:
                if path.endswith(hint) or path == hint:
                    score += 6
                    why.append(f"path {hint}")
                    break
                if hint in path:
                    score += 3
                    why.append(f"path contains {hint}")
                    break
            for hint in LABEL_HINTS:
                if hint and hint in label:
                    score += 4
                    why.append(f"link text {hint!r}")
                    break
            if first_label in DOCS_HOST_LABELS:
                score -= 6
                why.append("documentation host")
            for marker in DEMOTE_PATH_MARKERS:
                if marker in path:
                    score -= 4
                    break
            if score < MIN_CANDIDATE_SCORE:
                continue
            existing = scored.get(url)
            if existing is None or score > existing["score"]:
                scored[url] = {"url": url, "score": score, "why": ", ".join(why)}
    return sorted(scored.values(), key=lambda item: item["score"], reverse=True)


def classify(markdown: str, status: int | None) -> tuple[str, list[str], list[str]]:
    """What does this page show? Checked in order of what blocks you first."""
    body = (markdown or "").lower()
    signals: list[str] = []

    def hits(markers: tuple[str, ...]) -> list[str]:
        return [marker for marker in markers if marker in body]

    if status == 404:
        return "not_found", [f"HTTP {status}"], []
    if status in (401, 403, 407):
        return "login_wall", [f"HTTP {status}"], []

    fields = [field for field in FORM_FIELDS if field in body]
    login = hits(LOGIN_MARKERS)
    sales = hits(SALES_MARKERS)
    paid = hits(PAID_MARKERS)
    not_found = hits(NOT_FOUND_MARKERS)

    # A sign-in page that also mentions fields is still a sign-in page.
    if login and len(fields) < 3:
        return "login_wall", login[:4], fields
    if sales and len(fields) < 3:
        return "contact_sales", sales[:4], fields
    if paid:
        signals = paid[:4]
        return "paid_plan_required", signals, fields
    if len(fields) >= 3:
        observed = "application_form" if (sales or login) else "open_form"
        return observed, (sales or login)[:4], fields
    if not_found:
        return "not_found", not_found[:2], []
    return "unclear", (login or sales)[:4], fields


def probe(
    app_input: str,
    *,
    limit: int = DEFAULT_PROBE_LIMIT,
    use_cache: bool = True,
    progress: Callable[[str, str], None] | None = None,
) -> ProbeResult:
    def emit(message: str) -> None:
        if progress:
            progress("probe", message)

    slug = slugify(app_input)
    cached = read_json(slug_dir(slug) / "probe.json", default=None) if use_cache else None
    if cached:
        emit("cache hit")
        return ProbeResult.model_validate({**cached, "from_cache": True})

    pages = load_pages(slug)
    if not pages:
        emit("no cached pages; run discovery first")
        return ProbeResult(slug=slug)

    considered = candidate_urls(slug, pages)
    result = ProbeResult(slug=slug, considered=considered[:12])
    if not considered:
        emit("no app-creation link found on the scraped pages")

    for candidate in considered[:limit]:
        url = candidate["url"]
        emit(f"probing {url}")
        fetched, _ = scrape(url)
        content_type = (fetched.content_type or "").lower()
        if content_type and not any(kind in content_type for kind in TEXT_CONTENT):
            result.observations.append(
                Observation(
                    url=url,
                    observed="error",
                    at=utc_now(),
                    status=fetched.status,
                    source=fetched.source,
                    error=f"not a web page: {content_type}",
                    why=candidate["why"],
                )
            )
            emit(f"skipped: not a web page ({content_type})")
            continue
        if fetched.error and not fetched.markdown:
            result.observations.append(
                Observation(
                    url=url,
                    observed="error",
                    at=utc_now(),
                    status=fetched.status,
                    source=fetched.source,
                    error=fetched.error,
                    why=candidate["why"],
                )
            )
            emit(f"could not load: {fetched.error}")
            continue
        observed, signals, fields = classify(fetched.markdown or "", fetched.status)
        result.observations.append(
            Observation(
                url=url,
                observed=observed,
                at=utc_now(),
                status=fetched.status,
                source=fetched.source,
                signals=signals,
                fields_visible=fields,
                bytes=len((fetched.markdown or "").encode("utf-8")),
                why=candidate["why"],
            )
        )
        emit(f"{url} -> {observed}")

    write_json(slug_dir(slug) / "probe.json", result.model_dump(exclude={"from_cache"}))
    return result


DESCRIPTIONS = {
    "open_form": "the app registration form is open: its fields were visible without signing in",
    "application_form": "an application form is shown, behind a sign-in or an access request",
    "login_wall": "a sign-in wall: you must log in before you can register an app",
    "contact_sales": "no self-serve form; the page asks you to contact the provider for access",
    "paid_plan_required": "the page states a paid plan is needed",
    "not_found": "the expected app-creation page was not found",
    "unclear": "the page loaded but did not clearly show a form, a wall or a sales contact",
    "error": "the page could not be loaded",
}


def probe_facts(result: ProbeResult) -> list[Fact]:
    """Turn observations into Tested facts. Code writes these, not the model."""
    facts: list[Fact] = []
    for observation in result.observations:
        if observation.observed == "error":
            continue
        text = f"At {observation.url}, {DESCRIPTIONS[observation.observed]}."
        if observation.fields_visible:
            shown = ", ".join(observation.fields_visible[:8])
            text += f" Fields visible: {shown}."
        note = (
            f"observed by the agent at {observation.at}"
            f"{f', HTTP {observation.status}' if observation.status else ''}"
        )
        if observation.signals:
            note += f"; matched {', '.join(observation.signals[:4])}"
        facts.append(
            Fact(
                text=text,
                label=Label.TESTED,
                source_url=observation.url,
                note=note,
            )
        )
    return facts


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Stage 3: probe the developer portal.")
    parser.add_argument("app", help="app name or website")
    parser.add_argument("--limit", type=int, default=DEFAULT_PROBE_LIMIT)
    parser.add_argument("--no-cache", action="store_true")
    args = parser.parse_args(argv)

    result = probe(
        args.app,
        limit=args.limit,
        use_cache=not args.no_cache,
        progress=lambda stage, message: print(f"  [{stage}] {message}"),
    )
    print(f"\n{result.slug}{' - from cache' if result.from_cache else ''}")
    for observation in result.observations:
        print(f"  {observation.url}")
        print(f"    observed: {observation.observed}  (HTTP {observation.status}, "
              f"{observation.bytes} B via {observation.source})")
        print(f"    chosen because: {observation.why}")
        if observation.signals:
            print(f"    signals: {', '.join(observation.signals)}")
        if observation.fields_visible:
            print(f"    fields: {', '.join(observation.fields_visible[:10])}")
        print(f"    at: {observation.at}")
    print(f"\n  considered {len(result.considered)} candidate URLs")
    for item in result.considered[:6]:
        print(f"   - {item['score']:>2} {item['url']}  ({item['why']})")
    print("\nTested facts:")
    for fact in probe_facts(result):
        print(f"  [{fact.label.value}] {fact.text}")
        print(f"      note: {fact.note}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
