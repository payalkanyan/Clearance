"""Stage 6a: the rubric picks the highest level that genuinely applies."""

from __future__ import annotations

import pytest

from clearance.rubric import credentials_available_now, find_modifiers, score
from clearance.schema import Difficulty, Fact, Label


def fact(text: str, label: Label = Label.INFERRED) -> Fact:
    return Fact(text=text, label=label)


def facts(**sections) -> list[tuple[str, int | None, Fact]]:
    out: list[tuple[str, int | None, Fact]] = []
    for section, texts in sections.items():
        if isinstance(texts, str):
            out.append((section, None, fact(texts)))
        else:
            out += [(section, i, fact(t)) for i, t in enumerate(texts)]
    return out


def test_easy_when_nothing_gates_you():
    result = score(facts(verdict="Register an app and get credentials at once."))
    assert result.difficulty is Difficulty.EASY
    assert "nothing matched a harder level" in result.trigger


def test_medium_for_a_user_cap():
    result = score(facts(limits_before_approval=["Development mode allows up to 25 allowlisted users."]))
    assert result.difficulty is Difficulty.MEDIUM


def test_hard_for_a_mandatory_review():
    result = score(facts(approval_process=["Extending access requires a formal review."]))
    assert result.difficulty is Difficulty.HARD
    assert "formal review" in result.trigger


def test_very_hard_when_credentials_are_withheld():
    result = score(facts(approval_process=["You must contact sales before any credentials are issued."]))
    assert result.difficulty is Difficulty.VERY_HARD


def test_very_hard_is_ruled_out_when_keys_come_first():
    """The rubric's Very hard condition is approval before you get keys at all."""
    result = score(
        facts(
            verdict="Development mode credentials are created immediately without "
                    "approval, but unlimited users need a partner application.",
        )
    )
    assert result.difficulty is not Difficulty.VERY_HARD
    skipped = [m for m in result.matches if m.get("skipped")]
    assert any("approval before keys cannot apply" in m["skipped"] for m in skipped)


@pytest.mark.parametrize(
    "text",
    [
        "Organizations must apply for the Garmin Connect Developer Program to "
        "receive Starter Access credentials.",
        "You must be approved before you can register an application.",
        "Submit the application form and wait for a decision.",
        "To scale further, request enterprise access with your account manager.",
    ],
)
def test_a_programme_you_must_join_before_getting_keys_is_very_hard(text):
    result = score(facts(approval_process=[text]))
    assert result.difficulty is Difficulty.VERY_HARD


def test_an_optional_programme_does_not_set_the_level():
    result = score(
        facts(
            approval_process=[
                "Standard OAuth apps need no review.",
                "To list on GitHub Marketplace you must complete publisher verification.",
            ]
        )
    )
    assert result.difficulty is Difficulty.EASY
    assert any("optional programme" in m.get("skipped", "") for m in result.matches)


def test_a_denial_does_not_trigger_a_level():
    result = score(facts(approval_process=["No review is required before production use."]))
    assert result.difficulty is Difficulty.EASY
    assert any("negated by" in m.get("skipped", "") for m in result.matches)


def test_the_console_can_set_the_level_on_its_own():
    result = score(facts(verdict="Little is documented."), probe_observations=["contact_sales"])
    assert result.difficulty is Difficulty.VERY_HARD
    assert "contact_sales" in result.trigger


def test_modifiers_are_listed_but_do_not_change_the_level():
    result = score(facts(likely_blockers=["You must supply a privacy policy and a demo video."]))
    assert result.difficulty is Difficulty.EASY
    assert "Requires privacy policy or terms URLs" in result.modifiers
    assert "Requires a demo video or screencast" in result.modifiers


def test_a_modifier_from_an_optional_programme_is_skipped():
    found = find_modifiers(facts(likely_blockers=["Marketplace paid plans require a verified domain."]))
    assert found == []


@pytest.mark.parametrize(
    "text",
    ["Credentials are created immediately.", "Development mode is available.",
     "Keys are issued immediately after registering.", "No review is needed."],
)
def test_credentials_now_detection(text):
    assert credentials_available_now(facts(verdict=text)) is not None
