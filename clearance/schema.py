"""The guide schema, mirroring docs/guide-spec.md.

Two rules from the spec are enforced here rather than promised in a prompt:

* a fact labelled Sourced must carry both an official URL and a quote;
* a time estimate can never be labelled Tested.

Human-written guides (docs/gold/*.md) cite their sources in prose, so the
URL-and-quote requirement is relaxed for them by validating with
``context={"provenance": "human-gold"}``. It always binds agent output.
"""

from __future__ import annotations

import json
import re
from enum import StrEnum
from pathlib import Path
from typing import Iterator, Literal

from pydantic import BaseModel, ConfigDict, ValidationInfo, model_validator

QUOTE_MAX_WORDS = 25

# Sections whose facts are required for a guide to be useful. Skipped when the
# agent honestly found no OAuth support for the app.
REQUIRED_SECTIONS = (
    "prerequisites",
    "setup_steps",
    "limits_before_approval",
    "approval_process",
    "likely_blockers",
    "open_questions",
    "sources",
)

# Fields holding a single fact, in guide-spec order.
SINGLE_FACT_FIELDS = (
    "verdict",
    "difficulty_reason",
    "hands_on_time",
    "waiting_time",
    "composio_status",
)

# Fields holding a list of facts, in guide-spec order.
FACT_LIST_FIELDS = (
    "quick_setup_checklist",
    "prerequisites",
    "setup_steps",
    "scopes",
    "limits_before_approval",
    "approval_process",
    "likely_blockers",
    "open_questions",
)

TIME_FIELDS = ("hands_on_time", "waiting_time")


class Label(StrEnum):
    """How a claim was verified. See docs/guide-spec.md section 2."""

    TESTED = "Tested"
    SOURCED = "Sourced"
    INFERRED = "Inferred"
    UNCERTAIN = "Uncertain"


class Difficulty(StrEnum):
    """See docs/guide-spec.md section 3. Pick the highest level that applies.

    Unknown is an addition to the spec's four levels, used only when the app has
    no OAuth to rate. Calling that Easy would be a claim we cannot support.
    """

    EASY = "Easy"
    MEDIUM = "Medium"
    HARD = "Hard"
    VERY_HARD = "Very hard"
    UNKNOWN = "Unknown"


def _is_relaxed(info: ValidationInfo) -> bool:
    context = info.context or {}
    return context.get("provenance") == "human-gold"


class Fact(BaseModel):
    """One claim plus the evidence behind it."""

    model_config = ConfigDict(extra="forbid")

    text: str
    label: Label
    source_url: str | None = None
    quote: str | None = None
    note: str | None = None

    @model_validator(mode="after")
    def _check_evidence(self, info: ValidationInfo) -> "Fact":
        if self.label is not Label.SOURCED or _is_relaxed(info):
            return self
        missing = [
            name
            for name, value in (("source_url", self.source_url), ("quote", self.quote))
            if not (value or "").strip()
        ]
        if missing:
            raise ValueError(
                f"a Sourced fact needs {' and '.join(missing)} "
                f"(got {self.text[:70]!r}); use Inferred or Uncertain instead"
            )
        words = len(self.quote.split())
        if words > QUOTE_MAX_WORDS:
            raise ValueError(
                f"quote is {words} words, over the {QUOTE_MAX_WORDS}-word limit "
                f"(fact {self.text[:70]!r})"
            )
        return self

    def words_in_quote(self) -> int:
        return len((self.quote or "").split())


class Source(BaseModel):
    """A URL used to build the guide. Human guides may cite a title only."""

    model_config = ConfigDict(extra="forbid")

    url: str | None = None
    title: str | None = None

    @model_validator(mode="after")
    def _needs_something(self) -> "Source":
        if not (self.url or "").strip() and not (self.title or "").strip():
            raise ValueError("a source needs a url or at least a title")
        return self


class Verified(BaseModel):
    model_config = ConfigDict(extra="forbid")

    date: str
    by: Literal["agent", "human"]
    by_name: str | None = None
    note: str | None = None

    @model_validator(mode="after")
    def _check_date(self) -> "Verified":
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", self.date):
            raise ValueError(f"date must be YYYY-MM-DD, got {self.date!r}")
        return self


class Meta(BaseModel):
    model_config = ConfigDict(extra="forbid")

    slug: str
    provenance: Literal["agent", "human-gold"] = "agent"
    generated_at: str | None = None
    model: str | None = None
    no_oauth_found: bool = False


class Guide(BaseModel):
    """Fields in docs/guide-spec.md section 1 order."""

    model_config = ConfigDict(extra="forbid")

    app_name: str
    website: str
    verdict: Fact
    # The spec marks the checklist a future upgrade, so it stays optional.
    quick_setup_checklist: list[Fact] = []
    difficulty: Difficulty
    difficulty_reason: Fact | None = None
    hands_on_time: Fact
    waiting_time: Fact
    composio_status: Fact
    prerequisites: list[Fact] = []
    setup_steps: list[Fact] = []
    scopes: list[Fact] = []
    limits_before_approval: list[Fact] = []
    approval_process: list[Fact] = []
    likely_blockers: list[Fact] = []
    agent_can_do: list[str] = []
    you_must_do: list[str] = []
    open_questions: list[Fact] = []
    sources: list[Source] = []
    last_verified: Verified
    meta: Meta

    def iter_facts(self) -> Iterator[tuple[str, int | None, Fact]]:
        """Every fact in the guide as (section, index within section, fact)."""
        for field in SINGLE_FACT_FIELDS:
            fact = getattr(self, field)
            if fact is not None:
                yield field, None, fact
        for field in FACT_LIST_FIELDS:
            for index, fact in enumerate(getattr(self, field)):
                yield field, index, fact

    @model_validator(mode="after")
    def _times_are_never_tested(self) -> "Guide":
        for field in TIME_FIELDS:
            if getattr(self, field).label is Label.TESTED:
                raise ValueError(
                    f"{field} cannot be Tested: a time estimate counts as Tested "
                    "only if someone actually waited it out (guide-spec section 2)"
                )
        return self

    @model_validator(mode="after")
    def _cited_urls_are_listed(self) -> "Guide":
        """A URL good enough to cite belongs in Sources."""
        listed = {(source.url or "").rstrip("/") for source in self.sources}
        for _, _, fact in self.iter_facts():
            url = (fact.source_url or "").strip()
            if url and url.rstrip("/") not in listed:
                self.sources.append(Source(url=url))
                listed.add(url.rstrip("/"))
        return self

    @model_validator(mode="after")
    def _required_sections_present(self) -> "Guide":
        if self.meta.no_oauth_found:
            return self
        empty = [name for name in REQUIRED_SECTIONS if not getattr(self, name)]
        if empty:
            raise ValueError(
                f"these sections are empty: {', '.join(empty)}; set "
                "meta.no_oauth_found when the app has no OAuth to document"
            )
        return self


def load_guide(path: str | Path, *, provenance: str | None = None) -> Guide:
    """Read a guide from disk, relaxing citation rules for human-written ones."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    kind = provenance or data.get("meta", {}).get("provenance", "agent")
    return Guide.model_validate(data, context={"provenance": kind})
