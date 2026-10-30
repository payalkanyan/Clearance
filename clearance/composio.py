"""Stage 6b: is this app a Composio toolkit, and does Composio host the OAuth app?

The brief named docs.composio.dev/toolkits/managed-auth, but that page renders
its toolkit list in JavaScript, so scraping it answers nothing about a specific
app. The per-app page at composio.dev/toolkits/<slug> does: it returns 404 when
no toolkit exists, and when one does it states the managed-auth position in
prose we can quote. The docs page is still cached, once, for the definition.
"""

from __future__ import annotations

import re
from typing import Callable

from pydantic import BaseModel

from .cache import CACHE_DIR, PageRecord, read_json, store_page, write_json
from .config import slugify
from .fetch import scrape
from .schema import Fact, Label

# Composio's own hosts. Its pages are evidence about Composio, never about the
# provider whose console we want to open.
COMPOSIO_HOSTS = ("composio.dev",)

TOOLKIT_URL = "https://composio.dev/toolkits/{slug}"
MANAGED_AUTH_URL = "https://docs.composio.dev/toolkits/managed-auth"

# Where the one copy of the managed-auth page lives.
SHARED_DIR = CACHE_DIR / "_composio"

MANAGED_PATTERNS = (
    r"provides a managed OAuth app",
    r"managed OAuth app for",
    r"Composio[- ]managed OAuth",
    r"do not need to register an OAuth app",
)
# Checked after the managed patterns: a managed toolkit also mentions that you
# may optionally add your own app, and managed is the answer that matters.
BYO_PATTERNS = (
    r"bring your own OAuth app",
    r"must register an OAuth app",
    r"need your own OAuth app",
    r"register your own OAuth app",
    r"requires? .{0,40}your own OAuth app",
    r"go through your own OAuth app",
    r"add your own [A-Za-z ]*OAuth app",
)
API_KEY_PATTERNS = (
    r"uses an API key",
    r"requires an API key",
    r"API key to connect",
)

SENTENCE_END = re.compile(r"[.!?](?=\s|$)")
# A sentence boundary, allowing for the "+" these FAQ accordions leave behind:
# "...or OAuth app?+ Spotify requires connections to go through your own app."
SENTENCE_START = re.compile(r"[.!?]\+?\s+|\n")
# Markdown debris that means we grabbed page furniture, not a sentence.
DEBRIS = ("](", "##", "http", "|")
MAX_QUOTE_WORDS = 24


class ComposioStatus(BaseModel):
    slug: str
    kind: str  # managed | bring-your-own | toolkit-no-oauth | none | unknown
    url: str | None = None
    status: int | None = None
    tried: list[dict] = []
    quote: str | None = None
    pages: list[PageRecord] = []

    def as_fact(self) -> Fact:
        return build_fact(self)


def candidate_slugs(app_input: str) -> list[str]:
    """'Garmin Connect' -> garmin-connect, garminconnect, garmin."""
    slug = slugify(app_input)
    options = [slug, slug.replace("-", "")]
    if "-" in slug:
        options.append(slug.split("-")[0])
    seen: list[str] = []
    for option in options:
        if option and option not in seen:
            seen.append(option)
    return seen


def quote_around(markdown: str, match: re.Match) -> str | None:
    """A quote built around the matched phrase, not from the start of whatever
    the sentence splitter thought a sentence was.

    These pages put a whole FAQ answer after a run of link markup, so slicing
    the first words of a "sentence" can miss the match entirely.
    """
    boundaries = [found.end() for found in SENTENCE_START.finditer(markdown, 0, match.start())]
    start = boundaries[-1] if boundaries else match.start()

    def finish(text: str) -> str | None:
        collapsed = " ".join(text.split())
        end = SENTENCE_END.search(collapsed)
        if end:
            collapsed = collapsed[: end.end()]
        words = collapsed.split()
        return " ".join(words[:MAX_QUOTE_WORDS]) if words else None

    # Prefer the sentence the match sits in; fall back to the match onwards when
    # that sentence drags in page furniture.
    for candidate_start in (start, match.start()):
        window = markdown[candidate_start : candidate_start + 500]
        offset = match.end() - candidate_start
        tail = SENTENCE_END.search(window[offset:]) if offset < len(window) else None
        if tail:
            window = window[: offset + tail.end()]
        quote = finish(window)
        if quote and not any(bad in quote for bad in DEBRIS):
            return quote
    return None


def find_quote(markdown: str, patterns: tuple[str, ...]) -> str | None:
    """The fullest clean quote stating the position.

    Several patterns can match the same sentence at different offsets. The
    longest result is the one that still reads as a sentence; the shortest is a
    fragment starting mid-clause.
    """
    best: str | None = None
    for pattern in patterns:
        for match in re.finditer(pattern, markdown or "", re.I):
            quote = quote_around(markdown, match)
            if quote and (best is None or len(quote) > len(best)):
                best = quote
    return best


def classify(markdown: str) -> tuple[str, str | None]:
    """Managed beats bring-your-own: a managed toolkit also says you may bring
    your own app, and managed is the answer that matters."""
    from .citations import normalise

    page = normalise(markdown)
    for kind, patterns in (
        ("managed", MANAGED_PATTERNS),
        ("bring-your-own", BYO_PATTERNS),
        ("toolkit-no-oauth", API_KEY_PATTERNS),
    ):
        quote = find_quote(markdown, patterns)
        if not quote:
            continue
        # Stage 5 would catch this anyway; better not to claim it at all.
        return kind, (quote if normalise(quote) in page else None)
    return "unknown", None


def managed_auth_page(slug: str) -> PageRecord | None:
    """Cache the managed-auth docs page once, then reuse it for every app."""
    cached = SHARED_DIR / "managed-auth.md"
    if not cached.exists():
        fetched, _ = scrape(MANAGED_AUTH_URL)
        if not fetched.ok:
            return None
        cached.parent.mkdir(parents=True, exist_ok=True)
        cached.write_text(fetched.markdown or "", encoding="utf-8")
    return store_page(
        slug,
        MANAGED_AUTH_URL,
        cached.read_text(encoding="utf-8"),
        source="firecrawl",
        title="Managed OAuth apps | Composio",
        status=200,
        kind="composio",
    )


def lookup(
    app_input: str,
    *,
    use_cache: bool = True,
    progress: Callable[[str, str], None] | None = None,
) -> ComposioStatus:
    def emit(message: str) -> None:
        if progress:
            progress("composio", message)

    slug = slugify(app_input)
    cache_path = CACHE_DIR / slug / "composio.json"
    if use_cache:
        cached = read_json(cache_path, default=None)
        if cached:
            emit("cache hit")
            return ComposioStatus.model_validate(cached)

    status = ComposioStatus(slug=slug, kind="none")
    for candidate in candidate_slugs(app_input):
        url = TOOLKIT_URL.format(slug=candidate)
        emit(f"checking {url}")
        fetched, _ = scrape(url)
        status.tried.append(
            {"url": url, "status": fetched.status, "error": fetched.error}
        )
        if fetched.status == 404 or not fetched.ok:
            continue
        status.url = url
        status.status = fetched.status
        status.kind, status.quote = classify(fetched.markdown or "")
        page = store_page(
            slug,
            url,
            fetched.markdown or "",
            source=fetched.source,
            title=fetched.title,
            status=fetched.status,
            kind="composio",
        )
        status.pages = [page]
        definition = managed_auth_page(slug)
        if definition:
            status.pages.append(definition)
        emit(f"{candidate}: {status.kind}")
        break
    else:
        emit("no Composio toolkit page found")

    write_json(cache_path, status.model_dump())
    return status


DESCRIPTIONS = {
    "managed": (
        "Toolkit available with a Composio managed OAuth app, so you can connect "
        "without registering your own. Bringing your own app is optional, for your "
        "name on the consent screen."
    ),
    "bring-your-own": (
        "Toolkit available, but you must register your own OAuth app and give "
        "Composio its client ID and secret."
    ),
    "toolkit-no-oauth": (
        "Toolkit available, but it authenticates with an API key rather than OAuth."
    ),
    "unknown": (
        "A Composio toolkit page exists, but it does not state how authentication "
        "is provided."
    ),
    "none": "No Composio toolkit page found for this app.",
}


def build_fact(status: ComposioStatus) -> Fact:
    """Sourced when Composio's own page says it; otherwise honest about the gap."""
    text = DESCRIPTIONS[status.kind]
    if status.kind in ("managed", "bring-your-own", "toolkit-no-oauth") and status.quote:
        return Fact(
            text=text,
            label=Label.SOURCED,
            source_url=status.url,
            quote=status.quote,
            note="read from Composio's own toolkit page",
        )
    if status.kind in ("managed", "bring-your-own", "toolkit-no-oauth"):
        return Fact(
            text=text,
            label=Label.INFERRED,
            source_url=status.url,
            note="read from Composio's toolkit page, which states this without a "
                 "sentence that could be quoted cleanly",
        )
    if status.kind == "none":
        tried = ", ".join(item["url"] for item in status.tried) or "no URL tried"
        return Fact(
            text=text,
            label=Label.INFERRED,
            note=f"tried {tried}; a toolkit may exist under a different slug",
        )
    return Fact(
        text=text,
        label=Label.UNCERTAIN,
        source_url=status.url,
        note="the toolkit page did not state its authentication method",
    )


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Stage 6b: Composio status.")
    parser.add_argument("app")
    parser.add_argument("--no-cache", action="store_true")
    args = parser.parse_args(argv)

    status = lookup(
        args.app,
        use_cache=not args.no_cache,
        progress=lambda stage, message: print(f"  [{stage}] {message}"),
    )
    fact = status.as_fact()
    print(f"\n{status.slug}: {status.kind}")
    print(f"  [{fact.label.value}] {fact.text}")
    if fact.quote:
        print(f"      quote: {fact.quote!r}")
        print(f"      from:  {fact.source_url}")
    if fact.note:
        print(f"      note:  {fact.note}")
    for item in status.tried:
        print(f"  tried {item['url']} -> {item['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
