"""Stage 5: verify each Sourced quote against the page it cites.

No model is involved. A quote that cannot be found in the cached text of its
cited page loses the Sourced label and becomes Inferred, with a note saying why.
That is the check that makes Sourced mean something.

Both sides are normalised first, because a page's markdown and a model's quote
differ in ways that do not change the words: curly quotes, non-breaking spaces,
markdown emphasis, escaped underscores (Firecrawl writes `client\\_id`), and line
wrapping.
"""

from __future__ import annotations

import re
import unicodedata
from typing import Iterable

from pydantic import BaseModel

from .cache import load_pages, normalise_url, pages_text, slug_dir, write_json
from .config import slugify, utc_now
from .schema import Fact, Label

# Characters that differ between a page and a quote without changing the words.
LOOKALIKES = {
    "‘": "'", "’": "'", "‚": "'", "‛": "'",
    "“": '"', "”": '"', "„": '"', "«": '"', "»": '"',
    "–": "-", "—": "-", "―": "-", "−": "-",
    " ": " ", " ": " ", " ": " ", " ": " ",
    "​": "", "‌": "", "‍": "", "﻿": "",
    "…": "...",
}

MD_IMAGE = re.compile(r"!\[([^\]]*)\]\([^)]*\)")
MD_LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")
MD_ESCAPE = re.compile(r"\\([^A-Za-z0-9])")
MD_MARKS = re.compile(r"[*_`#>~|]")
WHITESPACE = re.compile(r"\s+")

# How much of a quote must match before we call it a near miss worth naming.
NEAR_MISS_WORDS = 8


class Downgrade(BaseModel):
    section: str
    index: int | None
    text: str
    reason: str
    source_url: str | None = None
    quote: str | None = None


class CheckResult(BaseModel):
    slug: str
    at: str
    checked: int = 0
    verified: int = 0
    downgrades: list[Downgrade] = []

    @property
    def ok(self) -> bool:
        return not self.downgrades


def normalise(text: str) -> str:
    """Fold away everything that is formatting rather than wording."""
    text = unicodedata.normalize("NFKC", text or "")
    for char, replacement in LOOKALIKES.items():
        text = text.replace(char, replacement)
    text = MD_IMAGE.sub(r"\1", text)
    text = MD_LINK.sub(r"\1", text)
    text = MD_ESCAPE.sub(r"\1", text)
    text = MD_MARKS.sub("", text)
    return WHITESPACE.sub(" ", text).strip().casefold()


def build_index(slug: str, pages=None) -> dict[str, str]:
    """Cited URL -> normalised page text, keyed so small URL differences match."""
    pages = pages if pages is not None else load_pages(slug)
    texts = pages_text(slug, pages)
    index: dict[str, str] = {}
    for page in pages:
        body = normalise(texts.get(page.url, ""))
        for key in {page.url, normalise_url(page.url), normalise_url(page.url).rstrip("/")}:
            index[key] = body
    return index


def lookup(url: str, index: dict[str, str]) -> str | None:
    for key in (url, normalise_url(url), normalise_url(url).rstrip("/")):
        if key in index:
            return index[key]
    return None


def verify(fact: Fact, index: dict[str, str]) -> str | None:
    """Return the reason a Sourced fact fails, or None when it holds up."""
    url = (fact.source_url or "").strip()
    if not url:
        return "no source_url"
    body = lookup(url, index)
    if body is None:
        return f"cited page was never scraped: {url}"
    quote = normalise(fact.quote or "")
    if not quote:
        return "no quote"
    if quote in body:
        return None
    words = quote.split()
    if len(words) > NEAR_MISS_WORDS:
        opening = " ".join(words[:NEAR_MISS_WORDS])
        if opening in body:
            return (
                f"quote does not appear in the cited page; its first "
                f"{NEAR_MISS_WORDS} words do, so the rest looks paraphrased or "
                "stitched together"
            )
    return "quote does not appear in the cited page"


def check(
    facts: Iterable[tuple[str, int | None, Fact]],
    index: dict[str, str],
    *,
    slug: str,
) -> CheckResult:
    """Downgrade every Sourced fact whose quote cannot be found. Mutates facts."""
    result = CheckResult(slug=slug, at=utc_now())
    for section, position, fact in facts:
        if fact.label is not Label.SOURCED:
            continue
        result.checked += 1
        reason = verify(fact, index)
        if reason is None:
            result.verified += 1
            continue
        result.downgrades.append(
            Downgrade(
                section=section,
                index=position,
                text=fact.text,
                reason=reason,
                source_url=fact.source_url,
                quote=fact.quote,
            )
        )
        fact.label = Label.INFERRED
        note = f"downgraded from Sourced on {result.at}: {reason}"
        fact.note = f"{fact.note} | {note}" if fact.note else note
    return result


def check_slug(slug: str, facts: Iterable[tuple[str, int | None, Fact]]) -> CheckResult:
    result = check(facts, build_index(slug), slug=slug)
    write_json(slug_dir(slug) / "citations.json", result.model_dump())
    return result


def main(argv: list[str] | None = None) -> int:
    import argparse

    from .extract import load_draft_facts

    parser = argparse.ArgumentParser(description="Stage 5: check Sourced quotes.")
    parser.add_argument("app", help="app name or website")
    args = parser.parse_args(argv)

    slug = slugify(args.app)
    facts = load_draft_facts(slug)
    if facts is None:
        print(f"no draft for {slug}; run: python -m clearance.extract {args.app!r}")
        return 1

    result = check_slug(slug, facts)
    print(f"{slug}: checked {result.checked} Sourced facts, "
          f"{result.verified} verified, {len(result.downgrades)} downgraded")
    for item in result.downgrades:
        where = f"{item.section}[{item.index}]" if item.index is not None else item.section
        print(f"\n  {where}: {item.reason}")
        print(f"    fact:  {item.text[:120]}")
        print(f"    quote: {item.quote!r}")
        print(f"    page:  {item.source_url}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
