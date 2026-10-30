"""Clearance UI.

Three views, all addressed by the URL (?view=...&app=<slug>), so any guide is a
shareable link and a reload shows the same thing.

A guide reads as a dossier: one narrow column, a strip of stat tiles, then the
sections in the order docs/guide-spec.md lists them. Every fact wears its
evidence label; the quote behind a label is one click away rather than always on
screen, so the prose stays readable without hiding the proof.

Colours come from .streamlit/config.toml, which redefines Streamlit's basic
colour slots to the palette in the README's architecture diagram. That is why
the labels here are native badges rather than hand-written HTML.
"""

from __future__ import annotations

import html

import streamlit as st

from clearance.config import GUIDES_DIR, base_url, slugify
from clearance.pipeline import run
from clearance.schema import Difficulty, Fact, Guide, Label, Source, load_guide

LABEL_BADGE = {
    Label.TESTED: "green",
    Label.SOURCED: "violet",
    Label.INFERRED: "orange",
    Label.UNCERTAIN: "gray",
}

LABEL_MEANING = {
    Label.TESTED: "The agent opened the page and recorded what was there.",
    Label.SOURCED: "An official page states this. The quote was checked against "
                   "that page's text.",
    Label.INFERRED: "Reasoned from the pages. No page states it outright.",
    Label.UNCERTAIN: "Nothing found, or the sources disagree.",
}

# Difficulty is a severity scale, so the meter fill carries severity and the
# unfilled track is a lighter step of the same hue. The level is always written
# out beside it: never colour alone.
DIFFICULTY_STEPS = {
    Difficulty.EASY: 1,
    Difficulty.MEDIUM: 2,
    Difficulty.HARD: 3,
    Difficulty.VERY_HARD: 4,
    Difficulty.UNKNOWN: 0,
}
DIFFICULTY_INK = {
    Difficulty.EASY: "#0F6E56",
    Difficulty.MEDIUM: "#8A6D00",
    Difficulty.HARD: "#9A3412",
    Difficulty.VERY_HARD: "#8B1D1D",
    Difficulty.UNKNOWN: "#5F5E5A",
}
DIFFICULTY_TRACK = {
    Difficulty.EASY: "#D7EDE5",
    Difficulty.MEDIUM: "#F2E6C2",
    Difficulty.HARD: "#F6DDD2",
    Difficulty.VERY_HARD: "#F3D7D7",
    Difficulty.UNKNOWN: "#E4E1D8",
}

STAGE_LABELS = {
    "input": "Checking the cache",
    "discover": "Finding and scraping the provider's pages",
    "probe": "Opening the app-creation page",
    "composio": "Looking up Composio status",
    "extract": "Writing the guide (the one model call)",
    "citations": "Checking every quote against its page",
    "score": "Applying the difficulty rubric",
    "write": "Saving the guide",
}

SECTIONS = (
    ("prerequisites", "Prerequisites", False),
    ("setup_steps", "Setup steps", True),
    ("scopes", "Scopes", False),
    ("limits_before_approval", "Limits before approval", False),
    ("approval_process", "Approval process", False),
    ("likely_blockers", "Likely blockers", False),
    ("open_questions", "Open questions", False),
)

CARD_CSS = """
<style>
  .cl-strip { display:flex; flex-wrap:wrap; gap:10px; margin:2px 0 6px; }
  .cl-strip-tight .cl-tile { flex:1 1 104px; padding:9px 11px; }
  .cl-strip-tight .cl-value { font-size:1.15rem; }
  .cl-tile { flex:1 1 150px; border:1px solid #E4E1D8; border-radius:8px;
             padding:12px 14px; background:#FFFDF9; }
  .cl-tile .cl-label { font-size:.72rem; letter-spacing:.06em;
             text-transform:uppercase; color:#6B6A64; }
  .cl-tile .cl-value { font-size:1.45rem; font-weight:600; line-height:1.25;
             margin-top:2px; font-family:system-ui,-apple-system,"Segoe UI",
             Roboto,Helvetica,Arial,sans-serif; }
  .cl-meter { display:flex; gap:3px; margin-top:9px; }
  .cl-seg { height:5px; flex:1; border-radius:3px; }
  .cl-quote { border-left:3px solid #E4E1D8; padding:2px 0 2px 12px;
             color:#4A4A46; font-size:.9rem; }
</style>
"""


def difficulty_tile(guide: Guide) -> str:
    level = guide.difficulty
    filled = DIFFICULTY_STEPS[level]
    ink, track = DIFFICULTY_INK[level], DIFFICULTY_TRACK[level]
    segments = "".join(
        f'<div class="cl-seg" style="background:{ink if i < filled else track}"></div>'
        for i in range(4)
    )
    return (
        '<div class="cl-tile">'
        '<div class="cl-label">Difficulty</div>'
        f'<div class="cl-value" style="color:{ink}">{html.escape(level.value)}</div>'
        f'<div class="cl-meter">{segments}</div>'
        "</div>"
    )


def plain_tile(label: str, value: str) -> str:
    return (
        '<div class="cl-tile">'
        f'<div class="cl-label">{html.escape(label)}</div>'
        f'<div class="cl-value">{html.escape(value)}</div>'
        "</div>"
    )


def stat_strip(guide: Guide) -> None:
    st.html(
        CARD_CSS
        + '<div class="cl-strip">'
        + difficulty_tile(guide)
        + plain_tile("Hands-on time", guide.hands_on_time.text)
        + plain_tile("Waiting time", guide.waiting_time.text)
        + "</div>"
    )


def badge(label: Label) -> str:
    return f":{LABEL_BADGE[label]}-badge[{label.value}]"


def evidence_tooltip(fact: Fact) -> str | None:
    """What sits behind the label, as a tooltip on the fact itself.

    A popover button per fact was tried and looked wrong: thirty controls
    scattered down the page, half of them wrapping onto their own line. The
    evidence belongs attached to the claim, not beside it.
    """
    parts = [f"**{fact.label.value}** — {LABEL_MEANING[fact.label]}"]
    if fact.quote:
        parts.append(f"> “{fact.quote}”")
    if fact.source_url:
        parts.append(fact.source_url)
    if fact.note:
        parts.append(f"_{fact.note}_")
    return "\n\n".join(parts) if len(parts) > 1 else None


def fact_row(fact: Fact, *, prefix: str = "", key: str = "") -> None:
    """One fact: its text, its label, and its evidence on hover."""
    st.markdown(
        f"{prefix}{fact.text} {badge(fact.label)}",
        help=evidence_tooltip(fact),
    )


def source_list(sources: list[Source]) -> None:
    for index, source in enumerate(sources, start=1):
        if source.url:
            st.markdown(f"{index}. [{source.title or source.url}]({source.url})")
        else:
            st.markdown(f"{index}. {source.title}")


def load_guides() -> list[Guide]:
    guides: list[Guide] = []
    for path in sorted(GUIDES_DIR.glob("*.json")):
        try:
            guides.append(load_guide(path))
        except Exception:  # a half-written file should not break the library
            continue
    return guides


def guide_for(slug: str) -> Guide | None:
    for candidate in (f"{slug}.json", f"{slug}.agent.json"):
        path = GUIDES_DIR / candidate
        if path.exists():
            return load_guide(path)
    return None


def share_url(slug: str) -> str:
    try:
        current = st.context.url or base_url()
    except Exception:
        current = base_url()
    return f"{current.split('?')[0].rstrip('/')}/?view=guide&app={slug}"


def go(view: str, slug: str | None = None) -> None:
    st.query_params["view"] = view
    if slug:
        st.query_params["app"] = slug
    elif "app" in st.query_params:
        del st.query_params["app"]


def render_guide_body(guide: Guide, slug: str) -> None:
    st.caption(guide.website)
    stat_strip(guide)

    st.markdown("##### Verdict")
    fact_row(guide.verdict, key=f"{slug}-verdict")
    if guide.difficulty_reason:
        with st.expander(f"Why {guide.difficulty.value}?"):
            st.caption(
                "The rubric in docs/guide-spec.md runs in code, not in the model. "
                "This is the fact that triggered the level."
            )
            fact_row(guide.difficulty_reason, key=f"{slug}-why")

    st.markdown("##### Composio")
    fact_row(guide.composio_status, key=f"{slug}-composio")

    for field, title, numbered in SECTIONS:
        facts = getattr(guide, field)
        if not facts:
            continue
        st.markdown(f"##### {title}")
        for position, fact in enumerate(facts, start=1):
            fact_row(
                fact,
                prefix=f"**{position}.** " if numbered else "",
                key=f"{slug}-{field}-{position}",
            )

    if guide.agent_can_do or guide.you_must_do:
        agent_column, human_column = st.columns(2, gap="medium", border=True)
        with agent_column:
            st.markdown("##### The agent can")
            for item in guide.agent_can_do:
                st.markdown(f"- {item}")
        with human_column:
            st.markdown("##### You must")
            for item in guide.you_must_do:
                st.markdown(f"- {item}")

    st.markdown(f"##### Sources ({len(guide.sources)})")
    source_list(guide.sources)

    verified = guide.last_verified
    st.divider()
    st.caption(
        f"Last verified {verified.date} by {verified.by_name or verified.by}"
        + (f", written by {guide.meta.model}" if guide.meta.model else "")
        + ". Quotes are checked against the cached text of the page they cite."
    )
    st.markdown("**Share this guide**")
    st.code(share_url(slug), language=None)


def library_page() -> None:
    st.title("Clearance")
    st.markdown(
        "How hard it is to get an OAuth app approved with a provider: the "
        "difficulty, the wait, what blocks you, and what you have to do "
        "yourself. Every claim carries an evidence label."
    )
    guides = load_guides()
    if not guides:
        st.info("No guides yet. Generate one from the Generate page.")
        return

    st.html(CARD_CSS)
    # A row at a time, so the cards line up instead of staggering down two
    # independent columns.
    for row_start in range(0, len(guides), 2):
        row = guides[row_start : row_start + 2]
        columns = st.columns(2, gap="medium")
        for offset, (column, guide) in enumerate(zip(columns, row)):
          with column.container(border=True, height="stretch"):
            origin = (
                ":violet-badge[hand-written]"
                if guide.meta.provenance == "human-gold"
                else ":gray-badge[agent]"
            )
            asked = (
                f" · asked for “{guide.meta.slug}”"
                if slugify(guide.app_name) != guide.meta.slug
                else ""
            )
            st.markdown(f"#### {guide.app_name}")
            st.markdown(f"{origin}{asked}")
            st.html(
                '<div class="cl-strip cl-strip-tight">'
                + difficulty_tile(guide)
                + plain_tile("Hands-on", guide.hands_on_time.text)
                + "</div>"
            )
            st.caption(
                guide.verdict.text[:130]
                + ("…" if len(guide.verdict.text) > 130 else "")
            )
            st.button(
                "Read the guide",
                # Two guides can share a slug: the gold GitHub one and the
                # agent's own.
                key=f"open-{guide.meta.slug}-{row_start + offset}",
                on_click=go,
                args=("guide", guide.meta.slug),
                width="stretch",
            )


def guide_page(slug: str) -> None:
    guide = guide_for(slug)
    if guide is None:
        st.error(f"No guide for {slug!r} yet.")
        st.button("Back to the library", on_click=go, args=("library",))
        return
    st.button("← Library", on_click=go, args=("library",), type="tertiary")
    st.title(guide.app_name)
    render_guide_body(guide, slug)


def generate_page() -> None:
    st.button("← Library", on_click=go, args=("library",), type="tertiary")
    st.title("Generate a guide")
    st.markdown(
        "Give an app name or a website. The stages run in order and only the "
        "extraction step calls a model, so a guide costs exactly one call."
    )
    with st.form("generate"):
        app_input = st.text_input("App name or website", placeholder="Notion")
        refresh = st.checkbox("Rebuild even if a guide already exists")
        submitted = st.form_submit_button("Generate", type="primary")

    if not submitted or not app_input.strip():
        return

    status = st.status(f"Building a guide for {app_input}", expanded=True)
    seen: set[str] = set()

    def progress(stage: str, message: str) -> None:
        if stage not in seen:
            seen.add(stage)
            status.write(f"**{STAGE_LABELS.get(stage, stage)}**")
        status.write(f"- {message}")

    try:
        result = run(app_input, refresh=refresh, progress=progress)
    except Exception as error:  # a failure must not take the page down
        status.update(label="Failed", state="error")
        st.error(f"{type(error).__name__}: {error}")
        return

    if result.error:
        status.update(label="Could not build a guide", state="error")
        st.error(result.error)
        return

    status.update(label=f"Guide ready for {result.guide.app_name}", state="complete")
    st.success(
        "Served from the saved guide."
        if result.from_cache
        else f"Saved to {result.guide_path}. The link at the bottom keeps working."
    )
    # The stage list stays above: what the agent did is part of the answer.
    st.title(result.guide.app_name)
    render_guide_body(result.guide, result.slug)


def main() -> None:
    st.set_page_config(page_title="Clearance", page_icon="🛂", layout="centered")
    view = st.query_params.get("view", "library")
    slug = st.query_params.get("app")

    with st.sidebar:
        st.markdown("### Clearance")
        st.button("Library", width="stretch", on_click=go, args=("library",))
        st.button("Generate", width="stretch", on_click=go, args=("generate",))
        st.divider()
        st.markdown("**Evidence labels**")
        for label in Label:
            st.markdown(f"{badge(label)} {LABEL_MEANING[label]}")

    if view == "guide" and slug:
        guide_page(slug)
    elif view == "generate":
        generate_page()
    else:
        library_page()


main()
