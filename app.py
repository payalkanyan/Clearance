"""Clearance UI: a library of guides, one guide per shareable link, and a
generate page that shows each stage as it runs.

State lives in the URL (?view=...&app=<slug>), so every guide is linkable and a
reload shows the same thing.
"""

from __future__ import annotations

import html

import streamlit as st

from clearance.config import GUIDES_DIR, base_url, slugify
from clearance.pipeline import run
from clearance.schema import Fact, Guide, Label, Source, load_guide

LABEL_COLOURS = {
    Label.TESTED: ("#0F6E56", "#E1F5EE"),
    Label.SOURCED: ("#3C3489", "#EEEDFE"),
    Label.INFERRED: ("#8A5A00", "#FDF2DD"),
    Label.UNCERTAIN: ("#444441", "#F1EFE8"),
}

DIFFICULTY_COLOURS = {
    "Easy": ("#0F6E56", "#E1F5EE"),
    "Medium": ("#8A5A00", "#FDF2DD"),
    "Hard": ("#9A3412", "#FDE8DC"),
    "Very hard": ("#8B1D1D", "#FBE2E2"),
    "Unknown": ("#444441", "#F1EFE8"),
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
    ("prerequisites", "Prerequisites"),
    ("setup_steps", "Setup steps"),
    ("scopes", "Scopes"),
    ("limits_before_approval", "Limits before approval"),
    ("approval_process", "Approval process"),
    ("likely_blockers", "Likely blockers"),
    ("open_questions", "Open questions"),
)


def tag(text: str, colours: tuple[str, str]) -> str:
    fore, back = colours
    return (
        f'<span style="background:{back};color:{fore};border-radius:4px;'
        f'padding:1px 6px;font-size:0.72rem;font-weight:600;white-space:nowrap">'
        f"{html.escape(text)}</span>"
    )


def label_tag(label: Label) -> str:
    return tag(label.value, LABEL_COLOURS[label])


def difficulty_tag(value: str) -> str:
    return tag(value, DIFFICULTY_COLOURS.get(value, DIFFICULTY_COLOURS["Unknown"]))


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
    root = current.split("?")[0].rstrip("/")
    return f"{root}/?view=guide&app={slug}"


def go(view: str, slug: str | None = None) -> None:
    st.query_params["view"] = view
    if slug:
        st.query_params["app"] = slug
    elif "app" in st.query_params:
        del st.query_params["app"]


def render_fact(fact: Fact) -> None:
    st.markdown(f"{label_tag(fact.label)} {html.escape(fact.text)}",
                unsafe_allow_html=True)
    if fact.quote and fact.source_url:
        st.markdown(
            f'<div style="margin:2px 0 10px 4px;padding-left:10px;'
            f'border-left:3px solid #e2e0d8;font-size:0.86rem;color:#4a4a46">'
            f"“{html.escape(fact.quote)}” — "
            f'<a href="{html.escape(fact.source_url)}" target="_blank">source</a></div>',
            unsafe_allow_html=True,
        )
    elif fact.note:
        st.caption(fact.note)


def source_list(sources: list[Source]) -> None:
    for source in sources:
        if source.url:
            st.markdown(f"- [{source.title or source.url}]({source.url})")
        else:
            st.markdown(f"- {source.title}")


def library_page() -> None:
    st.title("Clearance")
    st.caption(
        "How hard it is to get an OAuth app approved with a provider, with every "
        "claim labelled by how it was verified."
    )
    guides = load_guides()
    if not guides:
        st.info("No guides yet. Generate one from the Generate page.")
        return

    columns = st.columns(2)
    for index, guide in enumerate(guides):
        with columns[index % 2].container(border=True):
            badge = difficulty_tag(guide.difficulty.value)
            origin = (
                tag("hand-written", ("#3C3489", "#EEEDFE"))
                if guide.meta.provenance == "human-gold"
                else tag("agent", ("#444441", "#F1EFE8"))
            )
            st.markdown(f"### {html.escape(guide.app_name)}")
            st.markdown(f"{badge} &nbsp; {origin}", unsafe_allow_html=True)
            # The misspelled-input case resolves to the real provider name, so
            # say which input produced this guide.
            if slugify(guide.app_name) != guide.meta.slug:
                st.caption(f"asked for “{guide.meta.slug}”")
            st.markdown(f"**Hands-on:** {guide.hands_on_time.text}")
            st.markdown(f"**Waiting:** {guide.waiting_time.text}")
            st.caption(guide.verdict.text[:160])
            st.button(
                "Open guide",
                key=f"open-{guide.meta.slug}-{index}",
                on_click=go,
                args=("guide", guide.meta.slug),
            )


def render_guide_body(guide: Guide, slug: str) -> None:
    """The guide itself, shared by the guide page and the generate page."""
    st.markdown(f"**{guide.app_name}, {guide.website}**")

    left, middle, right = st.columns(3)
    left.markdown("**Difficulty**")
    left.markdown(difficulty_tag(guide.difficulty.value), unsafe_allow_html=True)
    middle.metric("Hands-on time", guide.hands_on_time.text)
    right.metric("Waiting time", guide.waiting_time.text)

    st.subheader("Verdict")
    render_fact(guide.verdict)
    if guide.difficulty_reason:
        with st.expander(f"Why {guide.difficulty.value}?"):
            render_fact(guide.difficulty_reason)

    st.subheader("Composio status")
    render_fact(guide.composio_status)

    for field, title in SECTIONS:
        facts = getattr(guide, field)
        if not facts:
            continue
        st.subheader(title)
        for position, fact in enumerate(facts, start=1):
            if field == "setup_steps":
                st.markdown(f"**{position}.**")
            render_fact(fact)

    if guide.agent_can_do or guide.you_must_do:
        agent_column, human_column = st.columns(2)
        with agent_column:
            st.subheader("Agent can do")
            for item in guide.agent_can_do:
                st.markdown(f"- {item}")
        with human_column:
            st.subheader("You must do")
            for item in guide.you_must_do:
                st.markdown(f"- {item}")

    st.subheader("Sources")
    source_list(guide.sources)

    verified = guide.last_verified
    st.caption(
        f"Last verified {verified.date} by {verified.by_name or verified.by}"
        + (f" using {guide.meta.model}" if guide.meta.model else "")
    )

    st.divider()
    st.markdown("**Share this guide**")
    st.code(share_url(slug), language=None)


def guide_page(slug: str) -> None:
    guide = guide_for(slug)
    if guide is None:
        st.error(f"No guide for {slug!r} yet.")
        st.button("Back to the library", on_click=go, args=("library",))
        return
    st.button("← Library", on_click=go, args=("library",))
    st.title(guide.app_name)
    render_guide_body(guide, slug)


def generate_page() -> None:
    st.button("← Library", on_click=go, args=("library",))
    st.title("Generate a guide")
    st.caption(
        "Give an app name or a website. Stages run in order; only the extraction "
        "step calls a model."
    )
    with st.form("generate"):
        app_input = st.text_input("App name or website", placeholder="Notion")
        refresh = st.checkbox("Rebuild even if a guide already exists")
        submitted = st.form_submit_button("Generate")

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
        f"Saved to {result.guide_path}. The link at the bottom keeps working."
        if not result.from_cache
        else "Served from the saved guide."
    )
    # The stage list stays above: what the agent did is part of the answer.
    st.header(result.guide.app_name)
    render_guide_body(result.guide, result.slug)
    st.button("Open the saved guide", on_click=go, args=("guide", result.slug))


def main() -> None:
    st.set_page_config(page_title="Clearance", page_icon="🛂", layout="centered")
    view = st.query_params.get("view", "library")
    slug = st.query_params.get("app")

    with st.sidebar:
        st.markdown("### Clearance")
        st.button("Library", use_container_width=True, on_click=go, args=("library",))
        st.button("Generate", use_container_width=True, on_click=go, args=("generate",))
        st.divider()
        st.caption("Evidence labels")
        for label in Label:
            st.markdown(label_tag(label), unsafe_allow_html=True)
        st.caption(
            "Tested: the agent opened the page. Sourced: an official page says it, "
            "with the quote checked against that page. Inferred: reasoned, not "
            "stated. Uncertain: nothing found."
        )

    if view == "guide" and slug:
        guide_page(slug)
    elif view == "generate":
        generate_page()
    else:
        library_page()


main()
