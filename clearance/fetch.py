"""Page fetching: Firecrawl first, the Anthropic web fetch tool as fallback.

The fallback drives `web_fetch` with a cheap model and then reads the page text
out of the tool-result block. The model's own prose is discarded, so no model
writing ever reaches a guide: stage 4 stays the only call that produces content.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Any
from urllib.parse import urlsplit

from pydantic import BaseModel

from .config import anthropic_api_key, fallback_mode, fetch_model, firecrawl_api_key

# Firecrawl failures worth retrying through web_fetch, per your Step 2 rules.
FALLBACK_KINDS = {"timeout", "rate_limit", "credits", "unavailable", "network"}

# A page this short with these markers is a wall, not content.
GATE_MARKERS = (
    "sign in",
    "log in",
    "login",
    "password",
    "create an account",
    "verify you are human",
    "enable javascript",
    "access denied",
    "checking your browser",
)
GATE_MAX_BYTES = 900

# A page this small carries no information. Usually a JavaScript-rendered page
# that returned its shell, and it would otherwise occupy a scrape slot and tell
# the model nothing.
MIN_USEFUL_BYTES = 500

MAX_CONTENT_TOKENS = 60_000


class FetchResult(BaseModel):
    url: str
    source: str  # "firecrawl" | "web_fetch"
    markdown: str | None = None
    title: str | None = None
    status: int | None = None
    links: list[str] = []
    content_type: str | None = None
    error: str | None = None
    error_kind: str | None = None
    usage: dict[str, Any] | None = None

    @property
    def ok(self) -> bool:
        return bool((self.markdown or "").strip()) and self.error is None


def host_of(url: str) -> str:
    return urlsplit(url).netloc.lower().removeprefix("www.")


def looks_like_gate(result: FetchResult) -> str | None:
    """Return a reason when the page is a login wall or bot check."""
    if result.status in (401, 403, 407):
        return f"HTTP {result.status}"
    body = (result.markdown or "").strip()
    if not body:
        return None
    if len(body.encode("utf-8")) <= GATE_MAX_BYTES:
        lowered = body.lower()
        hit = next((marker for marker in GATE_MARKERS if marker in lowered), None)
        if hit:
            return f"short page mentioning {hit!r}"
    return None


# Set when the configured key is rejected, so we only discover that once.
_keyless = False


@lru_cache(maxsize=2)
def _client(keyless: bool):
    from firecrawl import Firecrawl

    # Keyless works on a rate-limited free tier; a key raises the limits.
    return Firecrawl(api_key=None if keyless else firecrawl_api_key())


def firecrawl_client():
    return _client(_keyless or firecrawl_api_key() is None)


def firecrawl_degraded() -> bool:
    """True once we have fallen back to the keyless tier."""
    return _keyless


def note_key_rejected() -> None:
    global _keyless
    _keyless = True


def _classify(exc: Exception) -> str:
    import firecrawl

    mapping = (
        (firecrawl.RequestTimeoutError, "timeout"),
        (firecrawl.CrawlJobTimeoutError, "timeout"),
        (firecrawl.RateLimitError, "rate_limit"),
        (firecrawl.PaymentRequiredError, "credits"),
        (firecrawl.BadRequestError, "bad_request"),
        (firecrawl.DNSResolutionError, "network"),
        (firecrawl.TLSError, "network"),
        (firecrawl.InternalServerError, "unavailable"),
    )
    for kind, name in mapping:
        if isinstance(exc, kind):
            return name
    text = str(exc).lower()
    if "unauthorized" in text or "invalid token" in text or "401" in text:
        return "invalid_key"
    for needle, name in (
        ("timeout", "timeout"),
        ("rate limit", "rate_limit"),
        ("429", "rate_limit"),
        ("credit", "credits"),
        ("402", "credits"),
    ):
        if needle in text:
            return name
    return "other"


def firecrawl_scrape(url: str, *, timeout_ms: int = 45_000, max_age_ms: int = 86_400_000) -> FetchResult:
    result = _firecrawl_scrape_once(url, timeout_ms=timeout_ms, max_age_ms=max_age_ms)
    if result.error_kind == "invalid_key" and not firecrawl_degraded():
        note_key_rejected()
        result = _firecrawl_scrape_once(url, timeout_ms=timeout_ms, max_age_ms=max_age_ms)
    return result


def _firecrawl_scrape_once(
    url: str, *, timeout_ms: int, max_age_ms: int
) -> FetchResult:
    try:
        document = firecrawl_client().scrape(
            url,
            formats=["markdown", "links"],
            only_main_content=True,
            timeout=timeout_ms,
            max_age=max_age_ms,
        )
    except Exception as exc:  # the SDK raises typed errors; _classify sorts them
        return FetchResult(
            url=url, source="firecrawl", error=str(exc)[:300], error_kind=_classify(exc)
        )
    metadata = document.metadata
    status = getattr(metadata, "status_code", None)
    result = FetchResult(
        url=url,
        source="firecrawl",
        markdown=document.markdown,
        title=getattr(metadata, "title", None),
        status=status,
        links=list(document.links or [])[:300],
        content_type=getattr(metadata, "content_type", None),
    )
    if status and status >= 400:
        result.error = f"HTTP {status}"
        result.error_kind = "http_error"
    elif len((document.markdown or "").strip().encode("utf-8")) < MIN_USEFUL_BYTES:
        result.error = (
            f"page returned almost no content "
            f"({len((document.markdown or '').strip())} characters)"
        )
        result.error_kind = "empty"
    return result


def webfetch_scrape(url: str) -> FetchResult:
    """Fetch one page through the Anthropic web fetch tool.

    Only the tool result is read. `web_fetch_20250910` is deliberate: later
    versions filter content through code execution, which would make the cached
    text an unfaithful basis for the citation check.
    """
    if not anthropic_api_key():
        return FetchResult(
            url=url,
            source="web_fetch",
            error="ANTHROPIC_API_KEY is not set",
            error_kind="no_key",
        )
    try:
        import anthropic
    except ImportError:
        return FetchResult(
            url=url,
            source="web_fetch",
            error="the anthropic package is not installed",
            error_kind="no_sdk",
        )

    model = fetch_model()
    try:
        response = anthropic.Anthropic().messages.create(
            model=model,
            max_tokens=256,
            tools=[
                {
                    "type": "web_fetch_20250910",
                    "name": "web_fetch",
                    "max_uses": 1,
                    "allowed_domains": [host_of(url)],
                    "max_content_tokens": MAX_CONTENT_TOKENS,
                }
            ],
            messages=[{"role": "user", "content": f"Fetch {url} and reply with OK."}],
        )
    except Exception as exc:
        return FetchResult(
            url=url, source="web_fetch", error=str(exc)[:300], error_kind="api_error"
        )

    return parse_webfetch_payload(response.model_dump(), url, model)


def parse_webfetch_payload(payload: dict, url: str, model: str) -> FetchResult:
    """Read the page text out of the web_fetch tool result block."""
    usage = payload.get("usage") or {}
    result = FetchResult(
        url=url,
        source="web_fetch",
        usage={
            "model": model,
            "input_tokens": usage.get("input_tokens"),
            "output_tokens": usage.get("output_tokens"),
            "web_fetch_requests": (usage.get("server_tool_use") or {}).get(
                "web_fetch_requests"
            ),
        },
    )
    for block in payload.get("content") or []:
        if block.get("type") != "web_fetch_tool_result":
            continue
        content = block.get("content") or {}
        if content.get("type") == "web_fetch_tool_result_error":
            result.error = content.get("error_code") or "web_fetch error"
            result.error_kind = content.get("error_code")
            return result
        document = content.get("content") or {}
        source = document.get("source") or {}
        if source.get("type") != "text":
            result.error = f"unsupported content {source.get('media_type')}"
            result.error_kind = "unsupported_content_type"
            return result
        result.markdown = source.get("data")
        result.title = document.get("title")
        result.status = 200
        return result
    result.error = "no web_fetch result in the response"
    result.error_kind = "no_result"
    return result


STRIP_TAGS = ("script", "style", "nav", "footer", "noscript", "header", "aside",
              "form", "svg")

BROWSER_UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/131.0.0.0 Safari/537.36"
)


def http_scrape(url: str, *, timeout: float = 30.0) -> FetchResult:
    """Plain GET plus HTML to markdown. No model involved.

    This is the fallback when no Anthropic key is configured. It is weaker than
    Firecrawl on JavaScript-rendered and bot-protected pages, where it will
    usually produce a gate instead of text, which is the honest outcome.
    """
    import httpx
    from bs4 import BeautifulSoup
    from markdownify import markdownify

    try:
        response = httpx.get(
            url,
            follow_redirects=True,
            timeout=timeout,
            headers={"User-Agent": BROWSER_UA, "Accept": "text/html,*/*"},
        )
    except Exception as exc:
        return FetchResult(
            url=url, source="http", error=str(exc)[:300], error_kind="network"
        )

    content_type = response.headers.get("content-type", "")
    result = FetchResult(
        url=url,
        source="http",
        status=response.status_code,
        content_type=content_type or None,
    )
    if response.status_code >= 400:
        result.error = f"HTTP {response.status_code}"
        result.error_kind = "http_error"
        return result
    if "html" not in content_type and "text" not in content_type:
        result.error = f"unsupported content {content_type}"
        result.error_kind = "unsupported_content_type"
        return result

    soup = BeautifulSoup(response.text, "html.parser")
    for tag in soup(list(STRIP_TAGS)):
        tag.decompose()
    title = soup.title.get_text(strip=True) if soup.title else None
    result.markdown = markdownify(str(soup), heading_style="ATX").strip()
    result.title = title
    if len(result.markdown.encode("utf-8")) < MIN_USEFUL_BYTES:
        result.error = (
            f"page returned almost no content ({len(result.markdown)} characters)"
        )
        result.error_kind = "empty"
    return result


def choose_fallback() -> str:
    """web_fetch needs an Anthropic key; http always works."""
    mode = fallback_mode()
    if mode in ("web_fetch", "http"):
        return mode
    return "web_fetch" if anthropic_api_key() else "http"


def scrape(url: str) -> tuple[FetchResult, FetchResult | None]:
    """Firecrawl, then a fallback. Returns (result, the failed first attempt)."""
    first = firecrawl_scrape(url)
    if first.ok or first.error_kind not in FALLBACK_KINDS:
        return first, None
    fallback = webfetch_scrape if choose_fallback() == "web_fetch" else http_scrape
    return fallback(url), first
