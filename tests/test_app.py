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
    for heading in ("Verdict", "Composio", "Prerequisites", "Setup steps", "Sources"):
        assert f"##### {heading}" in text, heading
    assert "GitHub" in " ".join(block.value for block in result.title)


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


def test_labels_render_as_native_themed_badges():
    """The colours live in .streamlit/config.toml, so the labels are Streamlit
    badges rather than hand-written HTML spans."""
    result = app(view="guide", app="github")
    text = " ".join(block.value for block in result.markdown)
    assert ":violet-badge[Sourced]" in text
    assert ":green-badge[Tested]" in text
    assert "<span style=" not in text  # no hand-rolled chips left


def test_difficulty_shows_a_severity_meter_with_its_level_written_out():
    """Never colour alone: the level is always spelled out beside the meter."""
    result = app()
    blocks = " ".join(block.value for block in result.html)
    assert "cl-meter" in blocks and "cl-seg" in blocks
    assert "Difficulty" in blocks
    assert any(level in blocks for level in ("Easy", "Medium", "Hard", "Very hard"))


def test_a_guide_page_shows_the_three_stat_tiles():
    blocks = " ".join(block.value for block in app(view="guide", app="spotify").html)
    for label in ("Difficulty", "Hands-on time", "Waiting time"):
        assert label in blocks, label


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
    assert "##### Prerequisites" in reported
    assert any("view=guide&app=github" in block.value for block in result.code)


def test_a_guide_built_from_a_misspelled_input_says_so():
    """Two cards would otherwise both read "Spotify" with no way to tell them
    apart."""
    from clearance.config import GUIDES_DIR

    if not (GUIDES_DIR / "spotfy.json").exists():
        pytest.skip("the misspelled-input guide has not been generated")
    text = " ".join(block.value for block in app().markdown)
    assert "asked for" in text and "spotfy" in text
