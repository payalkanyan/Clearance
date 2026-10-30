"""Convert docs/gold/github.md into guides/github.json, keeping the human labels.

Run: python scripts/convert_gold.py [--write]

Prints a report of anything that did not fit the schema cleanly. Without
--write it is a dry run.
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from clearance.config import DOCS_DIR, GUIDES_DIR  # noqa: E402
from clearance.schema import (  # noqa: E402
    Difficulty,
    Fact,
    Guide,
    Label,
    Meta,
    Source,
    Verified,
)

GOLD = DOCS_DIR / "gold" / "github.md"
OUT = GUIDES_DIR / "github.json"

# "Hands-on time" -> the guide field that holds it.
INLINE_FIELDS = {
    "verdict": "verdict",
    "quick setup checklist": "quick_setup_checklist",
    "difficulty": "difficulty",
    "hands-on time": "hands_on_time",
    "waiting time": "waiting_time",
    "composio status": "composio_status",
    "scopes": "scopes",
    "limits before approval": "limits_before_approval",
    "approval process": "approval_process",
    "sources": "sources",
    "last verified": "last_verified",
}

BLOCK_FIELDS = {
    "prerequisites": "prerequisites",
    "setup steps": "setup_steps",
    "likely blockers and nuances": "likely_blockers",
    "agent can do": "agent_can_do",
    "you must do": "you_must_do",
    "open questions": "open_questions",
}

# Fields the schema wants as a list, which the gold writes as one line.
SINGLE_TO_LIST = {
    "quick_setup_checklist",
    "scopes",
    "limits_before_approval",
    "approval_process",
}

LABEL_WORDS = {label.value.lower(): label for label in Label}
LABEL_RE = re.compile(r"\b(tested|sourced|inferred|uncertain)\b", re.I)
ANNOTATION_RE = re.compile(r"\s*\*\(([^()]+)\)\*\s*$|\s*\(([^()]+)\)\s*$")

report: list[str] = []


def split_annotation(text: str) -> tuple[str, Label, str | None]:
    """Pull the trailing '*(Sourced; ...)*' off a line.

    Returns (text without it, primary label, the annotation kept verbatim).
    The primary label is the first one named; the whole annotation is kept as a
    note so nothing the author wrote is lost.
    """
    text = text.strip()
    match = ANNOTATION_RE.search(text)
    if not match:
        return text, Label.UNCERTAIN, None
    annotation = (match.group(1) or match.group(2)).strip()
    found = LABEL_RE.findall(annotation)
    if not found:
        # A parenthetical that is part of the sentence, e.g. "(any valid URL works)".
        return text, Label.UNCERTAIN, None
    label = LABEL_WORDS[found[0].lower()]
    stripped = text[: match.start()].rstrip()
    note = annotation if len(found) > 1 or len(annotation) > len(found[0]) + 1 else None
    if len(found) > 1:
        report.append(
            f"composite label {annotation!r} -> {label.value} as primary, "
            "full wording kept in note"
        )
    return stripped, label, note


def make_fact(text: str) -> Fact:
    body, label, note = split_annotation(text)
    # Relaxed context: the gold cites its sources in prose, not per fact.
    return Fact.model_validate(
        {"text": body, "label": label, "note": note},
        context={"provenance": "human-gold"},
    )


def parse_items(lines: list[str]) -> list[str]:
    """Bullet or numbered items, each possibly wrapped over several lines."""
    items: list[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        bullet = re.match(r"^(?:[-*]|\d+\.)\s+(.*)$", stripped)
        if bullet:
            items.append(bullet.group(1).strip())
        elif items:
            items[-1] += " " + stripped
    return items


def parse_last_verified(text: str) -> Verified:
    """'[Oct 29], by [0xpastril], the flow was confirmed.' -> a Verified."""
    raw = text.strip().rstrip(".")
    parts = [part.strip() for part in raw.split(",")]
    date_part = parts[0].strip("[]").strip()
    name = None
    extra: list[str] = []
    for part in parts[1:]:
        if part.lower().startswith("by "):
            name = part[3:].strip().strip("[]")
        elif part:
            extra.append(part)
    now = datetime.now(timezone.utc)
    try:
        parsed = datetime.strptime(f"{date_part} {now.year}", "%b %d %Y")
    except ValueError:
        parsed = datetime.strptime(f"{date_part} {now.year}", "%B %d %Y")
    if parsed.date() > now.date():  # "Oct 29" written in a past year
        parsed = parsed.replace(year=now.year - 1)
    if extra:
        report.append(
            f"'Last verified' carried extra prose {', '.join(extra)!r}; kept in note"
        )
    return Verified(
        date=parsed.strftime("%Y-%m-%d"),
        by="human",
        by_name=name,
        note=", ".join(extra) or None,
    )


def parse_sources(text: str) -> list[Source]:
    """The gold cites documents by name, not URL."""
    titles = [part.strip(" .") for part in text.split(";") if part.strip(" .")]
    report.append(
        f"'Sources' holds {len(titles)} prose citations with no URLs; "
        "stored as title-only sources"
    )
    return [Source(title=title) for title in titles]


def parse_gold(markdown: str) -> dict:
    lines = markdown.splitlines()
    data: dict = {}
    index = 0
    # Header: the first bold line that is not a labelled field.
    while index < len(lines):
        line = lines[index].strip()
        index += 1
        header = re.match(r"^\*\*([^*]+)\*\*$", line)
        if header and "," in header.group(1):
            app, _, website = header.group(1).partition(",")
            data["app_name"] = app.strip()
            data["website"] = website.strip()
            break

    pending_block: str | None = None
    block_lines: list[str] = []

    def flush() -> None:
        nonlocal pending_block, block_lines
        if pending_block:
            items = parse_items(block_lines)
            if pending_block in ("agent_can_do", "you_must_do"):
                data[pending_block] = items
            else:
                data[pending_block] = [make_fact(item) for item in items]
        pending_block, block_lines = None, []

    while index < len(lines):
        line = lines[index]
        index += 1
        stripped = line.strip()
        inline = re.match(r"^\*\*([^*:]+):\*\*\s*(.*)$", stripped)
        block = re.match(r"^\*\*([^*:]+)\*\*\s*$", stripped)
        if inline and inline.group(1).strip().lower() in INLINE_FIELDS:
            flush()
            field = INLINE_FIELDS[inline.group(1).strip().lower()]
            value = inline.group(2).strip()
            if field == "difficulty":
                data[field] = Difficulty(value.strip())
            elif field == "sources":
                data[field] = parse_sources(value)
            elif field == "last_verified":
                data[field] = parse_last_verified(value)
            else:
                fact = make_fact(value)
                data[field] = [fact] if field in SINGLE_TO_LIST else fact
        elif block and block.group(1).strip().lower() in BLOCK_FIELDS:
            flush()
            pending_block = BLOCK_FIELDS[block.group(1).strip().lower()]
        elif pending_block:
            block_lines.append(line)
    flush()
    return data


def main() -> int:
    markdown = GOLD.read_text(encoding="utf-8")
    data = parse_gold(markdown)

    # guide-spec section 2: a time estimate is Tested only if someone waited it out.
    for field in ("hands_on_time", "waiting_time"):
        fact = data.get(field)
        if fact and fact.label is Label.TESTED:
            original = fact.note or "Tested"
            fact.label = Label.INFERRED
            fact.note = (
                f"{original} | converted to Inferred: guide-spec section 2 says a "
                "time estimate is never Tested unless someone waited it out"
            )
            report.append(
                f"{field} was labelled Tested ({original!r}); converted to Inferred, "
                "original wording kept in note"
            )

    data["meta"] = Meta(
        slug="github",
        provenance="human-gold",
        generated_at=None,
        model=None,
        no_oauth_found=False,
    )

    guide = Guide.model_validate(data, context={"provenance": "human-gold"})

    unsourced = [
        f"{section}[{position}]" if position is not None else section
        for section, position, fact in guide.iter_facts()
        if fact.label is Label.SOURCED and not fact.source_url
    ]
    if unsourced:
        report.append(
            f"{len(unsourced)} Sourced facts carry no URL or quote "
            f"({', '.join(unsourced)}); allowed because this file is human-gold, "
            "but agent output would be rejected"
        )
    if guide.quick_setup_checklist:
        report.append(
            "'Quick setup checklist' is marked a future upgrade in guide-spec; "
            "kept as a one-item list so nothing is dropped"
        )

    payload = guide.model_dump(mode="json", exclude_none=True)
    if "--write" in sys.argv:
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    counts: dict[str, int] = {}
    for _, _, fact in guide.iter_facts():
        counts[fact.label.value] = counts.get(fact.label.value, 0) + 1
    total = sum(counts.values())

    print(f"{GOLD.relative_to(GOLD.parent.parent.parent)} -> {OUT.name}")
    print(f"  {total} facts: " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())))
    print(f"  difficulty {guide.difficulty.value}, "
          f"{len(guide.setup_steps)} setup steps, {len(guide.sources)} sources")
    print(f"  agent can do {len(guide.agent_can_do)}, you must do {len(guide.you_must_do)}")
    print()
    print(f"Did not fit cleanly ({len(report)}):")
    for item in report:
        print(f"  - {item}")
    if "--write" not in sys.argv:
        print("\n(dry run; pass --write to save)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
