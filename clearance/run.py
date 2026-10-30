"""CLI: python -m clearance.run "<app name or url>" """

from __future__ import annotations

import argparse
import json

from .pipeline import run
from .schema import Label

TAGS = {
    Label.TESTED: "Tested",
    Label.SOURCED: "Sourced",
    Label.INFERRED: "Inferred",
    Label.UNCERTAIN: "Uncertain",
}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m clearance.run",
        description="Build an OAuth setup guide for an app.",
    )
    parser.add_argument("app", help="app name or website")
    parser.add_argument("--refresh", action="store_true",
                        help="rebuild even if a guide already exists")
    parser.add_argument("--no-cache", action="store_true",
                        help="re-scrape pages instead of using the cache")
    parser.add_argument("--limit", type=int, default=7, help="pages to scrape")
    parser.add_argument("--model", default=None, help="override LLM_MODEL")
    parser.add_argument("--json", action="store_true", help="print the guide as JSON")
    parser.add_argument("--quiet", action="store_true", help="hide stage progress")
    args = parser.parse_args(argv)

    result = run(
        args.app,
        refresh=args.refresh,
        use_cache=not args.no_cache,
        limit=args.limit,
        model=args.model,
        progress=None if args.quiet else
        (lambda stage, message: print(f"  [{stage}] {message}")),
    )

    if result.error:
        print(f"\nFAILED ({result.slug}): {result.error}")
        return 1

    guide = result.guide
    if args.json:
        print(json.dumps(guide.model_dump(mode="json", exclude_none=True), indent=2))
        return 0

    counts: dict[str, int] = {}
    for _, _, fact in guide.iter_facts():
        counts[TAGS[fact.label]] = counts.get(TAGS[fact.label], 0) + 1

    print(f"\n{guide.app_name} - {guide.website}")
    print(f"  {guide.difficulty.value} | hands-on {guide.hands_on_time.text} | "
          f"waiting {guide.waiting_time.text}")
    print(f"  {guide.verdict.text}")
    print(f"  Composio: {guide.composio_status.text}")
    print(f"  facts: " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())))
    print(f"  {len(guide.setup_steps)} steps, {len(guide.likely_blockers)} blockers, "
          f"{len(guide.open_questions)} open questions, {len(guide.sources)} sources")
    if result.from_cache:
        print(f"  served from {result.guide_path}")
        return 0
    extract_log = result.log.get("extract", {})
    citations_log = result.log.get("citations", {})
    usage = extract_log.get("usage") or {}
    if not usage:
        print("  no model call: the guide was written in code because no OAuth "
              "evidence was found")
    elif extract_log.get("calls"):
        print(f"  one call to {result.log.get('model')}: "
              f"{usage.get('input_tokens')} in / {usage.get('output_tokens')} out, "
              f"${extract_log.get('cost_usd')} at list price")
    else:
        print(f"  no model call: reused the cached draft "
              f"({usage.get('input_tokens')} in / {usage.get('output_tokens')} out "
              f"when it was made)")
    if citations_log.get("checked") is not None:
        print(f"  quotes: {citations_log.get('verified')} of "
              f"{citations_log.get('checked')} verified, "
              f"{len(citations_log.get('downgrades', []))} downgraded")
    print(f"  {result.log['seconds']['total']}s total")
    print(f"  wrote {result.guide_path}, {result.markdown_path}, {result.log_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
