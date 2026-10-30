"""Stage 6a: the difficulty rubric, in code.

docs/guide-spec.md section 3 says to pick the highest level whose condition
applies, so this walks the levels from hardest down and stops at the first
match. The fact that triggered it is stored with the level, so a reader can
argue with the verdict instead of having to trust it.

A keyword rubric gets things wrong. That is why the trigger is recorded and why
stage 7 reports mismatches against expectations rather than forcing agreement.
"""

from __future__ import annotations

import re

from pydantic import BaseModel

from .schema import Difficulty, Fact

# Sections that say something about getting approved. Scopes and setup steps
# describe how to build, not what gates you.
GATING_SECTIONS = (
    "verdict",
    "waiting_time",
    "approval_process",
    "limits_before_approval",
    "likely_blockers",
)

# An optional programme is not a gate on using your own OAuth app. These are
# the words that make something optional: a paid tier, a badge, a verified
# publisher.
#
# "marketplace" is deliberately not here. For GitHub, listing is an extra you
# can skip; for Zoom, Marketplace review is how an app reaches anyone outside
# your own account. Treating the word itself as optional rated Zoom Easy
# despite six sourced facts about its multi-stage security review.
OPTIONAL_MARKERS = (
    "optional",
    "publisher verification",
    "badge",
    "paid plan",
    "paid plans",
    "if you want to list",
    "to offer paid",
    "verified publisher",
)

LEVEL_PATTERNS: dict[Difficulty, tuple[str, ...]] = {
    Difficulty.VERY_HARD: (
        r"contact (?:our )?sales",
        r"talk to sales",
        r"partner (?:program|programme|agreement|application)",
        r"become a partner",
        r"business (?:approval|agreement|verification)",
        r"security (?:audit|assessment|review|questionnaire)",
        r"penetration test",
        r"signed (?:agreement|contract)",
        r"letter of intent",
        r"before (?:you )?(?:can )?(?:receive|get|be issued) (?:any )?credentials",
        r"credentials are (?:only )?issued after",
        # "must apply for the X Developer Program to receive credentials": the
        # programme is the gate, and it stands before any keys exist.
        r"apply (?:for|to join) (?:the )?[a-z' ]{0,40}program",
        r"(?:to|and) receive [a-z' ]{0,40}credentials",
        r"request (?:enterprise|partner|elevated) access",
        r"approved before (?:you )?(?:can )?(?:register|create|receive|access)",
        r"application form",
        r"approval from (?:both|multiple|two)",
        r"invite[- ]only",
        r"by invitation",
    ),
    Difficulty.HARD: (
        r"(?:app|application) review",
        r"submit (?:your )?(?:app|application) for review",
        r"must be reviewed",
        r"review (?:is )?required",
        r"subject to review",
        r"verification (?:is )?required",
        r"must be verified",
        r"must complete .{0,40}verification",
        r"complete the .{0,30}verification process",
        r"questionnaire",
        r"assessment form",
        r"request production access",
        r"production access (?:requires|must)",
        r"apply for (?:production|full|extended|elevated)",
        r"approval (?:is )?required before",
        r"formal review",
        r"waitlist",
        r"request (?:to be )?(?:allow|white)listed",
        r"(?:allow|white)list request",
    ),
    Difficulty.MEDIUM: (
        r"development mode",
        r"dev mode",
        r"test mode",
        r"sandbox",
        r"quota mode",
        r"user (?:cap|limit)",
        r"up to \d+ [a-z ]{0,20}users",
        r"(?:allow|white)listed users",
        r"limited to \d+",
        r"request (?:an )?(?:extension|increase|quota)",
        r"extended quota",
        r"apply for more",
        r"raise (?:your )?(?:quota|limit)",
        r"restricted until",
    ),
}

# A pattern can match the very sentence that denies it: "created immediately
# without approval" contains "approval". Checked in a window around the match,
# so a later clause in the same sentence can still trigger a level.
NEGATORS = (
    "no review",
    "without review",
    "without approval",
    "no approval",
    "not require",
    "does not require",
    "no prior",
    "not reviewed",
)
NEGATION_WINDOW = 50


# These do not change the level. They belong in the blockers list.
MODIFIER_PATTERNS = {
    "Requires a paid plan": (r"paid plan", r"paid subscription", r"billing (?:is )?required",
                             r"requires a (?:paid|premium)"),
    "Requires a verified domain or company website": (r"verif(?:y|ied) (?:your )?domain",
                                                      r"domain verification", r"company website"),
    "Requires privacy policy or terms URLs": (r"privacy policy", r"terms of service url",
                                              r"terms url"),
    "Requires a demo video or screencast": (r"demo video", r"screencast", r"screen recording",
                                            r"video (?:of|showing) your"),
    "Regional or legal restrictions": (r"not available in", r"only available in",
                                       r"regional restriction", r"certain countries"),
}

# Evidence that you can get working credentials before anyone reviews anything.
# The rubric's Very hard condition is approval "before you get keys at all", so
# this rules that level out however partner-ish the production path sounds.
CREDENTIALS_NOW_PATTERNS = (
    r"credentials are created immediately",
    r"(?:keys|credentials|client secret) (?:are |is )?(?:available|issued|created|generated) immediately",
    r"immediately(?: after)? (?:register|creat)",
    r"without (?:any )?(?:prior )?approval",
    r"no review (?:is )?(?:needed|required)",
    r"development mode",
    r"dev mode",
    r"test mode",
    r"sandbox",
    r"self-serve",
    # "Private and beta apps require no review and can be used immediately":
    # whatever the public path demands, credentials exist before any review.
    r"require no review",
    r"requires? no (?:review|approval)",
    r"exempt from .{0,30}review",
    r"(?:can be )?used immediately",
    r"(?:private|internal|beta) apps?",
)

# What the agent saw at the console can settle the level on its own.
PROBE_LEVELS = {
    "contact_sales": Difficulty.VERY_HARD,
    "application_form": Difficulty.HARD,
}


class Score(BaseModel):
    difficulty: Difficulty
    reason: Fact | None = None
    trigger: str | None = None
    modifiers: list[str] = []
    matches: list[dict] = []


def _searchable(fact: Fact) -> str:
    return f"{fact.text} {fact.quote or ''}".lower()


def is_optional(text: str) -> bool:
    return any(marker in text for marker in OPTIONAL_MARKERS)


def is_negated(text: str, hit: re.Match) -> str | None:
    """Whether the words around the match deny what the pattern implies."""
    window = text[max(0, hit.start() - NEGATION_WINDOW) : hit.end() + NEGATION_WINDOW]
    return next((negator for negator in NEGATORS if negator in window), None)


def find_modifiers(facts: list[tuple[str, int | None, Fact]]) -> list[str]:
    """Modifiers a developer must satisfy. A requirement that only applies to an
    optional programme is not one of them."""
    found: list[str] = []
    for name, patterns in MODIFIER_PATTERNS.items():
        for _, _, fact in facts:
            text = _searchable(fact)
            if is_optional(text):
                continue
            if any(re.search(pattern, text) for pattern in patterns):
                found.append(name)
                break
    return found


def credentials_available_now(facts: list[tuple[str, int | None, Fact]]) -> str | None:
    """The phrase showing credentials arrive before any review, if one does."""
    for _, _, fact in facts:
        text = _searchable(fact)
        for pattern in CREDENTIALS_NOW_PATTERNS:
            hit = re.search(pattern, text)
            if hit:
                return hit.group(0)
    return None


def score(
    facts: list[tuple[str, int | None, Fact]],
    *,
    probe_observations: list[str] | None = None,
) -> Score:
    """Highest level whose condition applies, with the fact that triggered it."""
    gating = [
        (section, index, fact)
        for section, index, fact in facts
        if section in GATING_SECTIONS
    ]
    matches: list[dict] = []

    immediate = credentials_available_now(facts)
    levels = [Difficulty.VERY_HARD, Difficulty.HARD, Difficulty.MEDIUM]
    if immediate:
        levels.remove(Difficulty.VERY_HARD)
        matches.append(
            {
                "level": Difficulty.VERY_HARD.value,
                "skipped": f"credentials are available without approval ({immediate!r}), "
                           "so approval before keys cannot apply",
            }
        )

    for level in levels:
        for section, index, fact in gating:
            text = _searchable(fact)
            for pattern in LEVEL_PATTERNS[level]:
                hit = re.search(pattern, text)
                if not hit:
                    continue
                where = f"{section}[{index}]" if index is not None else section
                negator = is_negated(text, hit)
                if negator:
                    matches.append(
                        {
                            "level": level.value,
                            "pattern": pattern,
                            "where": where,
                            "skipped": f"negated by {negator!r} next to the match",
                        }
                    )
                    continue
                if is_optional(text):
                    matches.append(
                        {
                            "level": level.value,
                            "pattern": pattern,
                            "where": where,
                            "skipped": "describes an optional programme",
                        }
                    )
                    continue
                matches.append(
                    {"level": level.value, "pattern": pattern, "where": where,
                     "matched": hit.group(0)}
                )
                return Score(
                    difficulty=level,
                    reason=fact,
                    trigger=f"{where} matched {hit.group(0)!r}",
                    modifiers=find_modifiers(facts),
                    matches=matches,
                )

        # The console itself can be the evidence, once nothing stronger matched.
        for observed in probe_observations or []:
            if PROBE_LEVELS.get(observed) is level:
                matches.append({"level": level.value, "probe": observed})
                return Score(
                    difficulty=level,
                    reason=None,
                    trigger=f"the app-creation page showed {observed}",
                    modifiers=find_modifiers(facts),
                    matches=matches,
                )

    return Score(
        difficulty=Difficulty.EASY,
        reason=None,
        trigger="nothing matched a harder level: self-serve with no review found",
        modifiers=find_modifiers(facts),
        matches=matches,
    )
