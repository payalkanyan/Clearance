"""Stages 1 to 6, end to end.

Only stage 4 calls a model. Difficulty comes from the rubric in code, Composio
status from Composio's own page, and Tested facts from what the agent observed,
so the model cannot talk its way into any of them.
"""

from __future__ import annotations

import time
from collections import defaultdict
from typing import Callable

from pydantic import BaseModel, ValidationError

from . import composio as composio_module
from .cache import load_pages, normalise_url, read_json, save_pages, slug_dir, write_json
from .citations import build_index, check
from .config import GUIDES_DIR, LOGS_DIR, llm_model, slugify, today, utc_now
from .discover import DiscoveryResult, discover
from .extract import extract, iter_draft_facts
from .probe import probe, probe_facts
from .render import render
from .rubric import score
from .schema import Difficulty, Fact, Guide, Label, Meta, Source, Verified, load_guide

# Where an observation belongs in the guide, by what the agent saw.
PROBE_PLACEMENT = {
    "login_wall": "prerequisites",
    "application_form": "prerequisites",
    "open_form": "setup_steps",
    "contact_sales": "likely_blockers",
    "paid_plan_required": "likely_blockers",
    "not_found": "likely_blockers",
    "unclear": "open_questions",
}

FACT_SECTIONS = (
    "prerequisites",
    "setup_steps",
    "scopes",
    "limits_before_approval",
    "approval_process",
    "likely_blockers",
    "open_questions",
)


class RunResult(BaseModel):
    slug: str
    app_name: str
    guide: Guide | None = None
    guide_path: str | None = None
    markdown_path: str | None = None
    log_path: str | None = None
    from_cache: bool = False
    error: str | None = None
    log: dict = {}


def strip_scheme(url: str | None) -> str:
    return (url or "").split("://", 1)[-1].rstrip("/")


def guide_paths(slug: str) -> tuple[str, str]:
    """Never overwrite a human-written gold guide; write beside it instead."""
    existing = GUIDES_DIR / f"{slug}.json"
    if existing.exists():
        payload = read_json(existing, default={}) or {}
        if (payload.get("meta") or {}).get("provenance") == "human-gold":
            return f"{slug}.agent.json", f"{slug}.agent.md"
    return f"{slug}.json", f"{slug}.md"


def sources_from_pages(pages) -> list[Source]:
    return [Source(url=page.url, title=page.title) for page in pages]


def no_oauth_guide(
    discovery: DiscoveryResult, composio_fact: Fact, model: str | None
) -> Guide:
    """An honest guide for an app we found no OAuth evidence for."""
    queries = ", ".join(item["query"] for item in discovery.queries if item.get("query"))
    return Guide(
        app_name=discovery.app_name,
        website=strip_scheme(discovery.website),
        verdict=Fact(
            text="No OAuth app found. The provider's own pages we could read "
                 "describe no OAuth flow, so there may be nothing to register. "
                 "This app may authenticate with an API key instead.",
            label=Label.INFERRED,
            note=f"searched: {queries}; read "
                 f"{len([p for p in discovery.pages if p.official])} official pages",
        ),
        difficulty=Difficulty.UNKNOWN,
        difficulty_reason=Fact(
            text="The rubric rates OAuth approval, and no OAuth flow was found "
                 "to rate.",
            label=Label.INFERRED,
        ),
        hands_on_time=Fact(text="Unknown", label=Label.UNCERTAIN),
        waiting_time=Fact(text="Unknown", label=Label.UNCERTAIN),
        composio_status=composio_fact,
        open_questions=[
            Fact(
                text="Does this provider offer OAuth at all? If it does, the page "
                     "describing it was not among the search results.",
                label=Label.UNCERTAIN,
            )
        ],
        sources=sources_from_pages(discovery.pages),
        last_verified=Verified(date=today(), by="agent"),
        meta=Meta(
            slug=discovery.slug,
            generated_at=utc_now(),
            model=model,
            no_oauth_found=True,
        ),
    )


def run(
    app_input: str,
    *,
    refresh: bool = False,
    use_cache: bool = True,
    limit: int = 7,
    model: str | None = None,
    progress: Callable[[str, str], None] | None = None,
) -> RunResult:
    def emit(stage: str, message: str) -> None:
        if progress:
            progress(stage, message)

    slug = slugify(app_input)
    chosen_model = model or llm_model()
    result = RunResult(slug=slug, app_name=app_input.strip())
    timings: dict[str, float] = {}
    started = time.monotonic()

    # Stage 1: input and cache check. A finished guide is served as is.
    guide_name, markdown_name = guide_paths(slug)
    guide_file = GUIDES_DIR / guide_name
    if guide_file.exists() and not refresh:
        emit("input", f"serving the cached guide at guides/{guide_name}")
        result.guide = load_guide(guide_file)
        result.app_name = result.guide.app_name
        result.guide_path = str(guide_file)
        result.markdown_path = str(GUIDES_DIR / markdown_name)
        result.from_cache = True
        return result

    def timed(stage: str, call):
        clock = time.monotonic()
        value = call()
        timings[stage] = round(time.monotonic() - clock, 2)
        return value

    discovery = timed(
        "discover",
        lambda: discover(app_input, limit=limit, use_cache=use_cache,
                         progress=progress),
    )
    if discovery.failed:
        result.error = discovery.failed
        result.log = {"stage": "discover", "failed": discovery.failed,
                      "queries": discovery.queries}
        return result
    result.app_name = discovery.app_name

    probe_result = timed(
        "probe", lambda: probe(app_input, use_cache=use_cache, progress=progress)
    )
    composio_status = timed(
        "composio",
        lambda: composio_module.lookup(app_input, use_cache=use_cache,
                                       progress=progress),
    )
    composio_fact = composio_status.as_fact()

    # The Composio pages join the app's page set so stage 5 can check their quote.
    pages = list(discovery.pages)
    known = {normalise_url(page.url) for page in pages}
    for page in composio_status.pages:
        if normalise_url(page.url) not in known:
            pages.append(page)
            known.add(normalise_url(page.url))
    save_pages(slug, pages)

    if discovery.no_oauth_found:
        emit("extract", "skipped: no OAuth evidence, so there is nothing to write up")
        guide = no_oauth_guide(discovery, composio_fact, chosen_model)
        extraction = None
        citations = None
        rating = None
    else:
        extraction = timed(
            "extract",
            lambda: extract(
                app_input,
                app_name=discovery.app_name,
                probe_result=probe_result,
                composio_note=f"{composio_fact.text} (from {composio_status.url})"
                if composio_status.url
                else composio_fact.text,
                model=chosen_model,
                use_cache=use_cache,
                progress=progress,
            ),
        )
        if extraction.error or extraction.draft is None:
            result.error = extraction.error or "extraction produced nothing"
            result.log = {"stage": "extract", "failed": result.error}
            return result

        facts = list(iter_draft_facts(extraction.draft))
        # Composio's quote comes from a page too, so it is checked like any other.
        facts.append(("composio_status", None, composio_fact))
        citations = timed(
            "citations", lambda: check(facts, build_index(slug, pages), slug=slug)
        )
        emit("citations",
             f"{citations.verified} of {citations.checked} quotes verified, "
             f"{len(citations.downgrades)} downgraded")

        observations = probe_facts(probe_result)
        placed: dict[str, list[Fact]] = defaultdict(list)
        for observation, fact in zip(probe_result.observations, observations):
            placed[PROBE_PLACEMENT.get(observation.observed, "likely_blockers")].append(fact)

        singles: dict[str, Fact] = {}
        grouped: dict[str, list[Fact]] = defaultdict(list)
        for section, index, fact in facts:
            if index is None:
                singles[section] = fact
            else:
                grouped[section].append(fact)
        composio_fact = singles.pop("composio_status", composio_fact)
        for section, extra in placed.items():
            grouped[section] = extra + grouped[section]

        all_facts = [(section, None, fact) for section, fact in singles.items()]
        all_facts += [
            (section, index, fact)
            for section in FACT_SECTIONS
            for index, fact in enumerate(grouped[section])
        ]
        rating = timed(
            "score",
            lambda: score(
                all_facts,
                probe_observations=[o.observed for o in probe_result.observations],
            ),
        )
        emit("score", f"{rating.difficulty.value}: {rating.trigger}")

        reason = (
            Fact(
                text=rating.reason.text,
                label=rating.reason.label,
                source_url=rating.reason.source_url,
                quote=rating.reason.quote,
                note=f"triggered the {rating.difficulty.value} rating: {rating.trigger}",
            )
            if rating.reason
            else Fact(
                text=rating.trigger or "no rubric condition matched",
                label=Label.INFERRED,
                note="applied in code from the rubric in docs/guide-spec.md section 3",
            )
        )
        if rating.modifiers:
            grouped["likely_blockers"] += [
                Fact(text=item, label=Label.INFERRED,
                     note="rubric modifier: noted as a blocker, it does not change "
                          "the difficulty level")
                for item in rating.modifiers
            ]

        try:
            guide = Guide(
                app_name=extraction.draft.app_name or discovery.app_name,
                website=strip_scheme(extraction.draft.website or discovery.website),
                verdict=singles["verdict"],
                difficulty=rating.difficulty,
                difficulty_reason=reason,
                hands_on_time=singles["hands_on_time"],
                waiting_time=singles["waiting_time"],
                composio_status=composio_fact,
                prerequisites=grouped["prerequisites"],
                setup_steps=grouped["setup_steps"],
                scopes=grouped["scopes"],
                limits_before_approval=grouped["limits_before_approval"],
                approval_process=grouped["approval_process"],
                likely_blockers=grouped["likely_blockers"],
                agent_can_do=extraction.draft.agent_can_do,
                you_must_do=extraction.draft.you_must_do,
                open_questions=grouped["open_questions"],
                sources=sources_from_pages(pages),
                last_verified=Verified(date=today(), by="agent"),
                meta=Meta(slug=slug, generated_at=utc_now(), model=chosen_model),
            )
        except ValidationError as error:
            result.error = f"the assembled guide failed validation: {error}"
            result.log = {"stage": "assemble", "failed": result.error}
            return result

    GUIDES_DIR.mkdir(parents=True, exist_ok=True)
    write_json(guide_file, guide.model_dump(mode="json", exclude_none=True))
    markdown_file = GUIDES_DIR / markdown_name
    markdown_file.write_text(render(guide), encoding="utf-8")

    log = {
        "slug": slug,
        "app": discovery.app_name,
        "at": utc_now(),
        "model": chosen_model,
        "seconds": {**timings, "total": round(time.monotonic() - started, 2)},
        "discover": {
            "queries": discovery.queries,
            "pages": [
                {"url": page.url, "bytes": page.bytes, "source": page.source,
                 "official": page.official}
                for page in pages
            ],
            "gates": [gate.model_dump() for gate in discovery.gates],
            "fallbacks": discovery.fallbacks,
            "skipped": discovery.skipped,
            "no_oauth_found": discovery.no_oauth_found,
        },
        "probe": [o.model_dump() for o in probe_result.observations],
        "composio": {"kind": composio_status.kind, "tried": composio_status.tried},
        "extract": {
            "usage": extraction.usage if extraction else {},
            "cost_usd": extraction.cost_usd if extraction else 0.0,
            "prompt_chars": extraction.prompt_chars if extraction else 0,
            "trimmed": extraction.trimmed if extraction else [],
            "repairs": extraction.repairs if extraction else [],
            "calls": 1 if extraction else 0,
        },
        "citations": citations.model_dump() if citations else {},
        "score": rating.model_dump(mode="json") if rating else {},
    }
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    log_file = LOGS_DIR / f"{slug}.json"
    write_json(log_file, log)

    result.guide = guide
    result.guide_path = str(guide_file)
    result.markdown_path = str(markdown_file)
    result.log_path = str(log_file)
    result.log = log
    emit("write", f"wrote {guide_file.name}, {markdown_file.name} and logs/{slug}.json")
    return result
