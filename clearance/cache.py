"""On-disk cache, one directory per app under cache/<slug>/.

Pages are stored as markdown files plus a pages.json index. Stage 5 checks
quotes against these files, so what is stored must be what was fetched.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit, urlunsplit

from pydantic import BaseModel

from .config import CACHE_DIR, utc_now


class PageRecord(BaseModel):
    """One fetched page. `file` is relative to the app's cache directory."""

    url: str
    file: str
    source: str  # "firecrawl" | "web_fetch"
    fetched_at: str
    title: str | None = None
    status: int | None = None
    bytes: int = 0
    official: bool = True  # third-party pages can only support Inferred
    kind: str = "provider"  # "provider" | "composio"
    query: str | None = None


def normalise_url(url: str) -> str:
    """Drop the fragment and a trailing slash, lowercase the host."""
    parts = urlsplit(url.strip())
    path = parts.path.rstrip("/") or "/"
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path, parts.query, ""))


def url_key(url: str) -> str:
    return hashlib.sha1(normalise_url(url).encode("utf-8")).hexdigest()[:16]


def slug_dir(slug: str) -> Path:
    return CACHE_DIR / slug


def ensure_slug_dir(slug: str) -> Path:
    directory = slug_dir(slug)
    (directory / "pages").mkdir(parents=True, exist_ok=True)
    return directory


def read_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, default=str) + "\n", encoding="utf-8")


def load_pages(slug: str) -> list[PageRecord]:
    raw = read_json(slug_dir(slug) / "pages.json", default=[]) or []
    return [PageRecord.model_validate(item) for item in raw]


def save_pages(slug: str, pages: list[PageRecord]) -> None:
    write_json(slug_dir(slug) / "pages.json", [p.model_dump() for p in pages])


def store_page(
    slug: str,
    url: str,
    markdown: str,
    *,
    source: str,
    title: str | None = None,
    status: int | None = None,
    official: bool = True,
    kind: str = "provider",
    query: str | None = None,
) -> PageRecord:
    ensure_slug_dir(slug)
    relative = f"pages/{url_key(url)}.md"
    (slug_dir(slug) / relative).write_text(markdown, encoding="utf-8")
    return PageRecord(
        url=url,
        file=relative,
        source=source,
        fetched_at=utc_now(),
        title=title,
        status=status,
        bytes=len(markdown.encode("utf-8")),
        official=official,
        kind=kind,
        query=query,
    )


def page_text(slug: str, page: PageRecord) -> str:
    path = slug_dir(slug) / page.file
    return path.read_text(encoding="utf-8") if path.exists() else ""


def pages_text(slug: str, pages: list[PageRecord] | None = None) -> dict[str, str]:
    """url -> cached markdown, for the citation check and the extraction prompt."""
    pages = pages if pages is not None else load_pages(slug)
    return {page.url: page_text(slug, page) for page in pages}
