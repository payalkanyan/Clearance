"""Paths, environment and small shared helpers."""

from __future__ import annotations

import os
import re
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent

GUIDES_DIR = ROOT / "guides"
CACHE_DIR = ROOT / "cache"
LOGS_DIR = ROOT / "logs"
DOCS_DIR = ROOT / "docs"

load_dotenv(ROOT / ".env")


def _scrub_placeholders() -> None:
    """Remove .env.example's xxxx values from the environment.

    The Firecrawl and Anthropic SDKs read their keys from the environment on
    their own, so a placeholder left in place is sent as a real credential and
    comes back as "Invalid token".
    """
    for name in ("GEMINI_API_KEY", "GOOGLE_API_KEY", "ANTHROPIC_API_KEY",
                 "FIRECRAWL_API_KEY"):
        value = os.environ.get(name)
        if value and re.search(r"x{4,}", value, re.I):
            del os.environ[name]

_scrub_placeholders()

# Gemini, because it has a free tier. gemini-3.8-flash takes a 1,048,576 token
# input, which is ample for the pages one guide is built from.
DEFAULT_LLM_MODEL = "gemini-3.8-flash"

# Only used to drive the Anthropic web_fetch fallback, when a key is present.
DEFAULT_FETCH_MODEL = "claude-haiku-5-5"

# USD per million tokens (list price), for the cost line in logs/<slug>.json.
PRICES = {
    "gemini-3.8-flash": (0.75, 3.75),
    "gemini-3.6-flash": (0.75, 3.75),
    "gemini-3.5-flash-lite": (0.30, 2.50),
    "gemini-2.5-pro": (1.25, 10.00),
    "gemini-2.5-flash": (0.30, 2.50),
    "gemini-4-argon": (2.00, 10.00),
    "claude-haiku-5-5": (0.10, 0.50),
    "claude-opus-5-5": (4.00, 20.00),
}

# Models whose free tier can serve a whole run at no charge.
FREE_TIER = {
    "gemini-3.8-flash",
    "gemini-3.6-flash",
    "gemini-3.5-flash-lite",
    "gemini-2.5-pro",
    "gemini-2.5-flash",
}


def llm_model() -> str:
    return os.environ.get("LLM_MODEL") or DEFAULT_LLM_MODEL


def fetch_model() -> str:
    return os.environ.get("FETCH_MODEL") or DEFAULT_FETCH_MODEL


def looks_like_placeholder(value: str | None) -> bool:
    """True for the xxxx values in .env.example, so they count as unset."""
    return bool(value) and bool(re.search(r"x{4,}", value, re.I))


def _key(name: str) -> str | None:
    value = (os.environ.get(name) or "").strip()
    if not value or looks_like_placeholder(value):
        return None
    return value


def gemini_api_key() -> str | None:
    return _key("GEMINI_API_KEY") or _key("GOOGLE_API_KEY")


def anthropic_api_key() -> str | None:
    return _key("ANTHROPIC_API_KEY")


def fallback_mode() -> str:
    """How to fetch a page Firecrawl could not: auto, web_fetch or http."""
    return (os.environ.get("FALLBACK_MODE") or "auto").strip().lower()


def firecrawl_api_key() -> str | None:
    return _key("FIRECRAWL_API_KEY")


def base_url() -> str:
    return os.environ.get("BASE_URL") or "http://localhost:8501"


def estimate_cost(model: str, input_tokens: int, output_tokens: int) -> float | None:
    """List-price estimate for one call; a free-tier key may be billed nothing."""
    price = PRICES.get(model)
    if price is None:
        return None
    per_in, per_out = price
    return round(input_tokens / 1e6 * per_in + output_tokens / 1e6 * per_out, 6)


def utc_now() -> str:
    """Timestamp for probe evidence and guide metadata."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def slugify(name: str) -> str:
    """'Garmin Connect' -> 'garmin-connect'; a URL -> its host, minus www and TLD noise."""
    text = name.strip()
    if re.match(r"^[a-z][a-z0-9+.-]*://", text, re.I) or text.startswith("www."):
        text = re.sub(r"^[a-z][a-z0-9+.-]*://", "", text, flags=re.I)
        text = text.split("/")[0]
        text = re.sub(r"^(www|developer|developers|docs|api|dev)\.", "", text, flags=re.I)
        text = re.sub(r"\.(com|org|net|io|dev|co|app|ai|co\.uk)$", "", text, flags=re.I)
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "unknown"
