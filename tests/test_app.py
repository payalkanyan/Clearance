"""The UI runs without raising, on every route."""

from __future__ import annotations

from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest

TIMEOUT = 60
APP = str(Path(__file__).resolve().parent.parent / "app.py")


def app(**query) -> AppTest:
    test = AppTest.from_file(APP, default_timeout=TIMEOUT)
    for key, value in query.items():
        test.query_params[key] = value
    return test.run()


def test_library_lists_the_cached_guides():
    result = app()
    assert not result.exception
    headings = " ".join(block.value for block in result.markdown)
    assert "GitHub" in headings
    assert "Clearance" in " ".join(block.value for block in result.title)


def test_guide_page_renders_a_known_guide():
    result = app(view="guide", app="github")
    assert not result.exception
    text = " ".join(block.value for block in result.markdown)
    assert "Prerequisites" in " ".join(h.value for h in result.subheader)
    assert "Sources" in " ".join(h.value for h in result.subheader)
    assert "Tested" in text or "Sourced" in text


def test_guide_page_shows_a_shareable_link():
    result = app(view="guide", app="github")
    assert any("view=guide&app=github" in block.value for block in result.code)


def test_an_unknown_slug_does_not_crash_the_page():
    result = app(view="guide", app="not-a-real-app")
    assert not result.exception
    assert any("No guide" in block.value for block in result.error)


def test_generate_page_renders_its_form():
    result = app(view="generate")
    assert not result.exception
    assert result.text_input[0].label == "App name or website"
    assert result.button  # the submit button exists


def test_an_empty_submission_does_nothing():
    result = app(view="generate")
    result.text_input[0].set_value("").run()
    assert not result.exception
    assert not result.status


@pytest.mark.parametrize("label", ["Tested", "Sourced", "Inferred", "Uncertain"])
def test_the_sidebar_explains_every_label(label):
    result = app()
    sidebar = " ".join(block.value for block in result.sidebar.markdown)
    assert label in sidebar


def test_labels_render_as_coloured_tags():
    result = app(view="guide", app="github")
    html = " ".join(block.value for block in result.markdown)
    assert "border-radius:4px" in html  # the tag helper's styling reached the page
    assert "background:#E1F5EE" in html or "background:#EEEDFE" in html


def test_difficulty_renders_as_a_tag_on_the_library():
    html = " ".join(block.value for block in app().markdown)
    assert any(colour in html for colour in ("#E1F5EE", "#FDF2DD", "#FDE8DC", "#FBE2E2"))


def test_generating_a_guide_shows_each_stage_then_opens_it(monkeypatch):
    """The generate flow end to end, with the pipeline stubbed: no model call."""
    import clearance.pipeline as pipeline_module
    from clearance.pipeline import RunResult
    from clearance.schema import load_guide

    guide = load_guide("guides/github.json")
    stages = [
        ("discover", "kept 7 pages, 0 gates"),
        ("extract", "one call to gemini-3.8-flash"),
        ("citations", "29 of 29 quotes verified"),
        ("score", "Easy"),
    ]

    def fake_run(app_input, *, refresh=False, progress=None, **kwargs):
        for stage, message in stages:
            if progress:
                progress(stage, message)
        return RunResult(
            slug="github",
            app_name="GitHub",
            guide=guide,
            guide_path="guides/github.json",
            from_cache=False,
        )

    monkeypatch.setattr(pipeline_module, "run", fake_run)

    result = app(view="generate")
    result.text_input[0].set_value("GitHub")
    result.button[1].click().run()

    assert not result.exception
    reported = " ".join(block.value for block in result.markdown)
    assert "Finding and scraping the provider's pages" in reported
    assert "Writing the guide (the one model call)" in reported
    assert "29 of 29 quotes verified" in reported
    # The guide itself renders below the stage list, with its shareable link.
    assert "GitHub, github.com/settings/developers" in reported
    assert any("view=guide&app=github" in block.value for block in result.code)
