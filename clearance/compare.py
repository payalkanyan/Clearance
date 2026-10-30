"""Stage 7: diff the agent's guide against the hand-written one.

Facts are matched inside a section by text similarity, because the agent will
never phrase a step exactly the way a person did. Everything that does not match
is reported rather than explained away.

One bucket is separate on purpose: facts the human labelled Tested. The agent
cannot log in to a provider, so it can never reproduce those. Counting them as
failures would just add noise to every comparison.
"""

from __future__ import annotations

import difflib
import re

from pydantic import BaseModel

from .config import GUIDES_DIR
from .schema import Difficulty, Fact, Guide, Label, load_guide

# Above this, two sentences are talking about the same thing. Judged on content
# words as well as characters, because the agent writes longer sentences than a
# person and a character ratio alone punishes that far too hard.
SIMILARITY = 0.45

# Words that carry no meaning for matching purposes.
STOPWORDS = frozenset("""
a an the and or of to in on for with your you it its is are be can could may
must should will would that this these those if when while as at by from into
only also any each per not no none own own use used using need needs needed
""".split())

# Fields that hold exactly one fact, so the gold and the agent always correspond
# and the only question is how far apart they are.
SINGLE_SECTIONS = ("verdict", "hands_on_time", "waiting_time", "composio_status")

LIST_SECTIONS = (
    "prerequisites",
    "setup_steps",
    "scopes",
    "limits_before_approval",
    "approval_process",
    "likely_blockers",
    "open_questions",
)

COMPARED_SECTIONS = SINGLE_SECTIONS + LIST_SECTIONS

# Roughly what we expect, for reporting only. The rubric is never bent to agree.
EXPECTED_DIFFICULTY = {
    "github": Difficulty.EASY,
    "spotify": Difficulty.MEDIUM,
    "quickbooks": Difficulty.HARD,
    "garmin-connect": Difficulty.VERY_HARD,
}

WORD = re.compile(r"[a-z0-9]+")


class Pair(BaseModel):
    section: str
    gold_text: str
    agent_text: str
    gold_label: Label
    agent_label: Label
    similarity: float
    # True when the field had to pair (one value each) but the wording diverges.
    weak: bool = False

    @property
    def labels_agree(self) -> bool:
        return self.gold_label is self.agent_label


class Missing(BaseModel):
    section: str
    text: str
    label: Label
    human_only: bool = False


class Extra(BaseModel):
    section: str
    text: str
    label: Label


class Comparison(BaseModel):
    slug: str
    gold_path: str
    agent_path: str
    gold_difficulty: Difficulty
    agent_difficulty: Difficulty
    expected_difficulty: Difficulty | None = None
    matched: list[Pair] = []
    label_differences: list[Pair] = []
    missing: list[Missing] = []
    extra: list[Extra] = []
    human_only_missing: list[Missing] = []
    human_only_labels: list[Pair] = []

    @property
    def difficulty_agrees(self) -> bool:
        return self.gold_difficulty is self.agent_difficulty


def normalise(text: str) -> str:
    return " ".join(WORD.findall(text.lower()))


def content_words(text: str) -> set[str]:
    return {word for word in WORD.findall(text.lower())
            if word not in STOPWORDS and len(word) > 1}


def similarity(left: str, right: str) -> float:
    """The better of character overlap and content-word overlap (Dice)."""
    characters = difflib.SequenceMatcher(None, normalise(left), normalise(right)).ratio()
    first, second = content_words(left), content_words(right)
    if not first or not second:
        return characters
    dice = 2 * len(first & second) / (len(first) + len(second))
    return max(characters, dice)


def facts_by_section(guide: Guide) -> dict[str, list[Fact]]:
    sections: dict[str, list[Fact]] = {}
    for section, _, fact in guide.iter_facts():
        sections.setdefault(section, []).append(fact)
    return sections


def compare(slug: str) -> Comparison:
    gold_path = GUIDES_DIR / f"{slug}.json"
    agent_path = GUIDES_DIR / f"{slug}.agent.json"
    if not agent_path.exists():
        raise FileNotFoundError(
            f"no agent guide at {agent_path}; run: python -m clearance.run {slug!r}"
        )
    gold = load_guide(gold_path)
    agent = load_guide(agent_path)

    result = Comparison(
        slug=slug,
        gold_path=str(gold_path),
        agent_path=str(agent_path),
        gold_difficulty=gold.difficulty,
        agent_difficulty=agent.difficulty,
        expected_difficulty=EXPECTED_DIFFICULTY.get(slug),
    )

    gold_sections = facts_by_section(gold)
    agent_sections = facts_by_section(agent)

    for section in SINGLE_SECTIONS:
        gold_fact = (gold_sections.get(section) or [None])[0]
        agent_fact = (agent_sections.get(section) or [None])[0]
        if gold_fact is None or agent_fact is None:
            continue
        score = similarity(gold_fact.text, agent_fact.text)
        pair = Pair(
            section=section,
            gold_text=gold_fact.text,
            agent_text=agent_fact.text,
            gold_label=gold_fact.label,
            agent_label=agent_fact.label,
            similarity=round(score, 2),
            weak=score < SIMILARITY,
        )
        result.matched.append(pair)
        if not pair.labels_agree:
            result.label_differences.append(pair)

    for section in LIST_SECTIONS:  # noqa: PLR1702
        gold_facts = list(gold_sections.get(section, []))
        agent_facts = list(agent_sections.get(section, []))
        taken: set[int] = set()

        for gold_fact in gold_facts:
            best_index, best_score = None, 0.0
            for index, agent_fact in enumerate(agent_facts):
                if index in taken:
                    continue
                score = similarity(gold_fact.text, agent_fact.text)
                if score > best_score:
                    best_index, best_score = index, score
            if best_index is not None and best_score >= SIMILARITY:
                taken.add(best_index)
                agent_fact = agent_facts[best_index]
                pair = Pair(
                    section=section,
                    gold_text=gold_fact.text,
                    agent_text=agent_fact.text,
                    gold_label=gold_fact.label,
                    agent_label=agent_fact.label,
                    similarity=round(best_score, 2),
                )
                result.matched.append(pair)
                if not pair.labels_agree:
                    # Only a human who ran the flow can label a step Tested.
                    if pair.gold_label is Label.TESTED:
                        result.human_only_labels.append(pair)
                    else:
                        result.label_differences.append(pair)
            else:
                missing = Missing(
                    section=section,
                    text=gold_fact.text,
                    label=gold_fact.label,
                    human_only=gold_fact.label is Label.TESTED,
                )
                if missing.human_only:
                    result.human_only_missing.append(missing)
                else:
                    result.missing.append(missing)

        for index, agent_fact in enumerate(agent_facts):
            if index not in taken:
                result.extra.append(
                    Extra(section=section, text=agent_fact.text, label=agent_fact.label)
                )
    return result


def report(result: Comparison) -> str:
    lines = [
        f"Comparing {result.agent_path} against {result.gold_path}",
        "",
        f"Difficulty: gold {result.gold_difficulty.value}, "
        f"agent {result.agent_difficulty.value}"
        + ("  (agree)" if result.difficulty_agrees else "  (MISMATCH)"),
    ]
    if result.expected_difficulty:
        agrees = result.agent_difficulty is result.expected_difficulty
        lines.append(
            f"Expected {result.expected_difficulty.value}: "
            + ("agent agrees" if agrees else f"agent said {result.agent_difficulty.value}")
        )
    lines += [
        "",
        f"Matched facts:        {len(result.matched)}"
        + (f"  ({len([p for p in result.matched if p.weak])} same field, "
           f"different wording)" if any(p.weak for p in result.matched) else ""),
        f"Label differences:    {len(result.label_differences)}",
        f"Missing (gold only):  {len(result.missing)}",
        f"Extra (agent only):   {len(result.extra)}",
        f"Human-only Tested:    {len(result.human_only_missing)} missing, "
        f"{len(result.human_only_labels)} matched but relabelled"
        "   (the agent cannot log in, so Tested is out of reach)",
    ]

    weak = [pair for pair in result.matched if pair.weak]
    if weak:
        lines += ["", "Same field, wording far apart"]
        for pair in weak:
            lines += [
                f"  {pair.section} (similarity {pair.similarity})",
                f"    gold:  {pair.gold_text[:110]}",
                f"    agent: {pair.agent_text[:110]}",
            ]
    if result.label_differences:
        lines += ["", "Label differences"]
        for pair in result.label_differences:
            lines += [
                f"  {pair.section}: gold {pair.gold_label.value} -> "
                f"agent {pair.agent_label.value}  (similarity {pair.similarity})",
                f"    gold:  {pair.gold_text[:110]}",
                f"    agent: {pair.agent_text[:110]}",
            ]
    if result.missing:
        lines += ["", "In the gold guide, not found by the agent"]
        for item in result.missing:
            lines.append(f"  [{item.label.value}] {item.section}: {item.text[:110]}")
    if result.human_only_missing or result.human_only_labels:
        lines += ["", "Human-only Tested facts the agent could not reproduce"]
        for item in result.human_only_missing:
            lines.append(f"  {item.section}: {item.text[:110]}")
        for pair in result.human_only_labels:
            lines.append(
                f"  {pair.section}: found and labelled {pair.agent_label.value} "
                f"instead: {pair.agent_text[:80]}"
            )
    if result.extra:
        lines += ["", "Found by the agent, not in the gold guide"]
        for item in result.extra:
            lines.append(f"  [{item.label.value}] {item.section}: {item.text[:110]}")
    return "\n".join(lines)


def difficulty_table() -> str:
    """Every cached agent guide against its expected level."""
    rows = [f"{'app':<16}{'expected':<12}{'agent':<12}{'':<8}trigger"]
    for path in sorted(GUIDES_DIR.glob("*.json")):
        guide = load_guide(path)
        if guide.meta.provenance == "human-gold":
            continue
        expected = EXPECTED_DIFFICULTY.get(guide.meta.slug)
        verdict = (
            "-"
            if expected is None
            else ("agrees" if guide.difficulty is expected else "MISMATCH")
        )
        trigger = (guide.difficulty_reason.note or guide.difficulty_reason.text
                   if guide.difficulty_reason else "")
        rows.append(
            f"{guide.meta.slug:<16}{(expected.value if expected else '-'):<12}"
            f"{guide.difficulty.value:<12}{verdict:<10}{trigger[:70]}"
        )
    return "\n".join(rows)


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Stage 7: compare against the gold guide.")
    parser.add_argument("slug", nargs="?", default="github")
    parser.add_argument("--difficulty", action="store_true",
                        help="print the difficulty table for every cached guide")
    args = parser.parse_args(argv)

    if args.difficulty:
        print(difficulty_table())
        return 0
    print(report(compare(args.slug)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
