"""Stage 4: the one LLM call per guide.

Everything else in Clearance is code or tools. This call reads the scraped
pages and writes the guide's prose.

Two rules are enforced structurally rather than asked for politely:

* the draft schema's label enum offers only Sourced, Inferred and Uncertain, so
  the model cannot emit Tested at all. Tested facts come from stage 3, where the
  agent actually opened a page;
* a Sourced fact that does not cite one of the supplied official pages, or
  carries no quote, is repaired in code afterwards. There is no second call.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Callable, Literal

from pydantic import BaseModel

from .cache import PageRecord, load_pages, page_text, slug_dir, write_json
from .config import estimate_cost, gemini_api_key, llm_model, slugify
from .probe import ProbeResult, probe_facts
from .schema import QUOTE_MAX_WORDS, Fact, Label

# Enough of each page to carry the OAuth story, without letting one giant
# reference table (GitHub's permissions page is 585 KB) crowd out the rest.
PER_PAGE_CHARS = 40_000
TOTAL_CHARS = 240_000

MAX_OUTPUT_TOKENS = 16_000

DraftLabel = Literal["Sourced", "Inferred", "Uncertain"]


class DraftFact(BaseModel):
    text: str
    label: DraftLabel
    source_url: str | None = None
    quote: str | None = None
    note: str | None = None


class GuideDraft(BaseModel):
    """What the model is asked for. Difficulty and Composio status are not here:
    the rubric is applied in code in stage 6, and Composio status is looked up."""

    app_name: str
    website: str
    verdict: DraftFact
    hands_on_time: DraftFact
    waiting_time: DraftFact
    prerequisites: list[DraftFact]
    setup_steps: list[DraftFact]
    scopes: list[DraftFact]
    limits_before_approval: list[DraftFact]
    approval_process: list[DraftFact]
    likely_blockers: list[DraftFact]
    agent_can_do: list[str]
    you_must_do: list[str]
    open_questions: list[DraftFact]


FACT_LIST_FIELDS = (
    "prerequisites",
    "setup_steps",
    "scopes",
    "limits_before_approval",
    "approval_process",
    "likely_blockers",
    "open_questions",
)
SINGLE_FACT_FIELDS = ("verdict", "hands_on_time", "waiting_time")

SYSTEM_INSTRUCTION = f"""\
You write setup guides for developers who need to create and get approval for an
OAuth app with a provider. You are given pages scraped from that provider's own
documentation, plus notes on what an agent observed when it opened the
provider's app-creation page.

The verdict is about getting approved with the provider itself: how quickly you
can register an app, and what review stands between you and real users. It is
not about Composio. Composio's position is recorded separately and must not
appear in the verdict or be restated as a fact of your own.

Write only what the supplied pages support. Never use knowledge from memory as
if it came from a page. Never invent a step, a time, a limit or a URL.

Every fact carries an evidence label:

- Sourced: the pages state it. Requires source_url set to the exact URL of the
  supplied page that states it, and quote set to a span of at most
  {QUOTE_MAX_WORDS} words copied character-for-character from that page. Do not
  paraphrase a quote, do not stitch together two parts of a page, and do not
  quote a page marked THIRD-PARTY.
- Inferred: a reasonable reading of the pages, or general knowledge, that no
  page states outright. Say what the inference rests on in note.
- Uncertain: the pages conflict, look outdated, or say nothing. Prefer this over
  guessing. A guide that admits a gap is more useful than one that fills it in.

A claim with no supporting page is Uncertain, never Sourced.

Other rules:

- hands_on_time and waiting_time are ranges in plain words, such as "5 to 15
  minutes" or "2 to 6 weeks". Use "Unknown" when nothing supports a number.
  These are estimates, so they are never Sourced unless a page states the
  figure itself.
- setup_steps go in the order a developer performs them, each a single concrete
  action. Include the console URL, the redirect URI field name and the scopes
  where the pages give them. At most 12 steps.
- scopes names the few scopes a typical integration asks for and says how and
  when they are requested. At most 6 entries: summarise, do not reproduce the
  provider's whole scope table.
- limits_before_approval covers user caps, test or development modes, rate
  limits and sandbox-only data that apply before any review.
- approval_process covers what is reviewed, what you submit, and who decides.
- likely_blockers covers what commonly causes rejection or delay: a required
  paid plan, a verified domain, privacy policy or terms URLs, a demo video,
  regional restrictions, organisation policies.
- agent_can_do and you_must_do are short plain strings, no labels. An agent can
  read docs, explain scopes and fill in a guide. A human must log in, click
  consent, handle secrets and submit review forms.
- open_questions names what remains genuinely unresolved after reading the
  pages. At most 5.
- Keep prerequisites, limits_before_approval, approval_process and
  likely_blockers to at most 6 entries each, strongest first. A guide is read by
  a developer in a hurry.

Do not restate the agent's observations, or Composio's position, as facts of
your own: both are already recorded separately. They are context, so that your
setup steps can mention pasting credentials into Composio where that applies.
"""


@lru_cache(maxsize=1)
def gemini_client():
    """Held for the process: a client that goes out of scope closes its
    transport, and an in-flight request then fails."""
    from google import genai

    return genai.Client()


class ExtractionResult(BaseModel):
    slug: str
    model: str
    draft: GuideDraft | None = None
    usage: dict = {}
    cost_usd: float | None = None
    prompt_chars: int = 0
    trimmed: list[dict] = []
    repairs: list[str] = []
    error: str | None = None


def build_pages_block(
    slug: str, pages: list[PageRecord]
) -> tuple[str, list[dict], list[str]]:
    """The scraped pages as prompt text, with what was trimmed and the citable URLs."""
    blocks: list[str] = []
    trimmed: list[dict] = []
    citable: list[str] = []
    spent = 0
    for index, page in enumerate(pages, start=1):
        if spent >= TOTAL_CHARS:
            trimmed.append({"url": page.url, "kept_chars": 0, "reason": "prompt full"})
            continue
        body = page_text(slug, page)
        allowance = min(PER_PAGE_CHARS, TOTAL_CHARS - spent)
        kept = body[:allowance]
        if len(kept) < len(body):
            trimmed.append(
                {
                    "url": page.url,
                    "kept_chars": len(kept),
                    "original_chars": len(body),
                    "reason": "per-page cap" if allowance == PER_PAGE_CHARS else "prompt full",
                }
            )
        spent += len(kept)
        origin = "OFFICIAL" if page.official else "THIRD-PARTY (Inferred at best)"
        if page.official:
            citable.append(page.url)
        blocks.append(f"## PAGE {index} [{origin}]\nURL: {page.url}\n\n{kept}")
    return "\n\n".join(blocks), trimmed, citable


def website_for(pages: list[PageRecord], probe: ProbeResult | None) -> str | None:
    """Where a developer actually goes: the console if we probed one, else the
    provider's own documentation host."""
    if probe and probe.observations:
        observation = probe.observations[0]
        return observation.url.split("://", 1)[-1]
    official = next((page.url for page in pages if page.official), None)
    return official.split("://", 1)[-1].split("/")[0] if official else None


def build_input(
    app_name: str,
    website: str | None,
    pages_block: str,
    probe: ProbeResult | None,
    composio_note: str | None,
) -> str:
    parts = [
        f"App: {app_name}",
        f"Website: {website or 'unknown'}",
        "",
        "Write the guide for this app from the pages below.",
    ]
    observations = probe_facts(probe) if probe else []
    if observations:
        parts += ["", "# What the agent observed on the provider's own pages", ""]
        parts += [f"- {fact.text} ({fact.note})" for fact in observations]
    if composio_note:
        parts += ["", "# Composio", "", composio_note]
    parts += ["", "# Pages", "", pages_block]
    return "\n".join(parts)


def repair(draft: GuideDraft, citable: list[str]) -> tuple[GuideDraft, list[str]]:
    """Fix label violations in code. A second call would break the one-call rule."""
    repairs: list[str] = []
    allowed = {url.rstrip("/") for url in citable}

    def fix(fact: DraftFact, where: str) -> DraftFact | None:
        if not fact.text.strip():
            repairs.append(f"{where}: dropped, empty text")
            return None
        if fact.label != "Sourced":
            return fact
        url = (fact.source_url or "").strip()
        quote = (fact.quote or "").strip()
        reason = None
        if not url:
            reason = "no source_url"
        elif url.rstrip("/") not in allowed:
            reason = f"cites {url}, which is not one of the official pages supplied"
        elif not quote:
            reason = "no quote"
        if reason:
            fact.label = "Inferred"
            fact.note = f"{fact.note + ' | ' if fact.note else ''}downgraded from Sourced: {reason}"
            repairs.append(f"{where}: Sourced -> Inferred ({reason})")
            return fact
        words = quote.split()
        if len(words) > QUOTE_MAX_WORDS:
            fact.quote = shorten_quote(quote)
            repairs.append(
                f"{where}: quote trimmed from {len(words)} to "
                f"{len(fact.quote.split())} words"
            )
        return fact

    for field in SINGLE_FACT_FIELDS:
        fixed = fix(getattr(draft, field), field)
        if fixed is None:  # a required single fact cannot just vanish
            fixed = DraftFact(text="Unknown", label="Uncertain", note="model returned nothing")
        setattr(draft, field, fixed)

    for field in FACT_LIST_FIELDS:
        kept: list[DraftFact] = []
        for index, fact in enumerate(getattr(draft, field)):
            fixed = fix(fact, f"{field}[{index}]")
            if fixed is not None:
                kept.append(fixed)
        setattr(draft, field, kept)

    # A time estimate can never be Sourced-by-inference; guide-spec section 2
    # also forbids Tested, which the schema already prevents.
    return draft, repairs


def shorten_quote(quote: str) -> str:
    """Cut an over-long quote to a sentence end where possible, else a word
    boundary. Either way the result stays a verbatim prefix, so stage 5 can
    still find it in the page."""
    limit = QUOTE_MAX_WORDS - 1
    words = quote.split()
    for end in range(min(limit, len(words)), 0, -1):
        if words[end - 1].endswith((".", "!", "?")):
            return " ".join(words[:end])
    return " ".join(words[:limit])


def to_fact(fact: DraftFact) -> Fact:
    return Fact(
        text=fact.text,
        label=Label(fact.label),
        source_url=fact.source_url,
        quote=fact.quote,
        note=fact.note,
    )


def iter_draft_facts(draft: GuideDraft):
    """Every fact in a draft as (section, index, Fact), like Guide.iter_facts."""
    for field in SINGLE_FACT_FIELDS:
        yield field, None, to_fact(getattr(draft, field))
    for field in FACT_LIST_FIELDS:
        for index, fact in enumerate(getattr(draft, field)):
            yield field, index, to_fact(fact)


def load_draft_facts(slug: str) -> list[tuple[str, int | None, Fact]] | None:
    """The cached draft's facts, for running stage 5 on its own."""
    from .cache import read_json

    payload = read_json(slug_dir(slug) / "draft.json", default=None)
    if not payload or not payload.get("draft"):
        return None
    return list(iter_draft_facts(GuideDraft.model_validate(payload["draft"])))


def extract(
    app_input: str,
    *,
    app_name: str | None = None,
    probe_result: ProbeResult | None = None,
    composio_note: str | None = None,
    model: str | None = None,
    use_cache: bool = True,
    progress: Callable[[str, str], None] | None = None,
) -> ExtractionResult:
    def emit(message: str) -> None:
        if progress:
            progress("extract", message)

    slug = slugify(app_input)
    chosen = model or llm_model()
    result = ExtractionResult(slug=slug, model=chosen)

    if use_cache:
        from .cache import read_json

        cached = read_json(slug_dir(slug) / "draft.json", default=None)
        if cached and cached.get("draft") and cached.get("model") == chosen:
            emit("cache hit: reusing the draft, no call made")
            previous = ExtractionResult.model_validate(cached)
            previous.usage = {**previous.usage, "calls": 0}
            return previous

    if not gemini_api_key():
        result.error = "GEMINI_API_KEY is not set"
        return result
    if not chosen.startswith("gemini"):
        result.error = (
            f"LLM_MODEL is {chosen!r}; this build calls the Gemini API, so set a "
            "gemini-* model"
        )
        return result

    pages = load_pages(slug)
    if not pages:
        result.error = "no cached pages; run discovery first"
        return result

    pages_block, result.trimmed, citable = build_pages_block(slug, pages)
    if not citable:
        result.error = "no official pages to cite"
        return result

    # "GitHub", not "Github": prefer what the caller typed over a slug.
    name = app_name or (app_input.strip() if not app_input.startswith("http") else slug.title())
    website = website_for(pages, probe_result)
    prompt = build_input(name, website, pages_block, probe_result, composio_note)
    result.prompt_chars = len(prompt)
    emit(f"one call to {chosen} with {len(pages)} pages ({len(prompt):,} chars)")

    try:
        interaction = gemini_client().interactions.create(
            model=chosen,
            system_instruction=SYSTEM_INSTRUCTION,
            input=[{"type": "text", "text": prompt}],
            response_format={
                "type": "text",
                "mime_type": "application/json",
                "schema": GuideDraft.model_json_schema(),
            },
            generation_config={"max_output_tokens": MAX_OUTPUT_TOKENS},
        )
    except Exception as exc:
        result.error = f"{type(exc).__name__}: {str(exc)[:300]}"
        return result

    usage = interaction.usage
    result.usage = {
        "input_tokens": getattr(usage, "total_input_tokens", None),
        "output_tokens": getattr(usage, "total_output_tokens", None),
        "total_tokens": getattr(usage, "total_tokens", None),
        "calls": 1,
    }
    result.cost_usd = estimate_cost(
        chosen, result.usage["input_tokens"] or 0, result.usage["output_tokens"] or 0
    )

    try:
        draft = GuideDraft.model_validate_json(interaction.output_text)
    except Exception as exc:
        result.error = f"output did not match the schema: {str(exc)[:300]}"
        return result

    result.draft, result.repairs = repair(draft, citable)
    emit(f"{len(result.repairs)} repairs, {result.usage['input_tokens']} input tokens")
    write_json(slug_dir(slug) / "draft.json", result.model_dump())
    return result


def main(argv: list[str] | None = None) -> int:
    import argparse

    from .probe import probe

    parser = argparse.ArgumentParser(description="Stage 4: the one LLM call.")
    parser.add_argument("app", help="app name or website")
    parser.add_argument("--model", default=None)
    args = parser.parse_args(argv)

    slug = slugify(args.app)
    probe_result = probe(slug, use_cache=True)
    result = extract(
        args.app,
        probe_result=probe_result,
        model=args.model,
        progress=lambda stage, message: print(f"  [{stage}] {message}"),
    )
    if result.error:
        print(f"\nFAILED: {result.error}")
        return 1

    draft = result.draft
    print(f"\n{draft.app_name} ({draft.website})")
    print(f"  verdict: [{draft.verdict.label}] {draft.verdict.text}")
    print(f"  hands-on: [{draft.hands_on_time.label}] {draft.hands_on_time.text}")
    print(f"  waiting:  [{draft.waiting_time.label}] {draft.waiting_time.text}")
    for field in FACT_LIST_FIELDS:
        facts = getattr(draft, field)
        print(f"\n  {field} ({len(facts)}):")
        for fact in facts:
            print(f"    [{fact.label}] {fact.text[:140]}")
            if fact.quote:
                print(f"        quote: {fact.quote!r}")
                print(f"        from:  {fact.source_url}")
    print(f"\n  agent can do: {draft.agent_can_do}")
    print(f"  you must do:  {draft.you_must_do}")
    print(f"\n  usage: {result.usage}  cost: ${result.cost_usd}")
    print(f"  prompt: {result.prompt_chars:,} chars, trimmed {len(result.trimmed)} pages")
    for item in result.trimmed:
        print(f"    - {item['url']}: kept {item['kept_chars']:,} "
              f"of {item.get('original_chars', '?')} ({item['reason']})")
    print(f"  repairs ({len(result.repairs)}):")
    for item in result.repairs:
        print(f"    - {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
