"""Transport behaviour: error classification, gates, web_fetch parsing."""

from __future__ import annotations

import firecrawl
import pytest

from clearance.fetch import (
    FetchResult,
    _classify,
    looks_like_gate,
    parse_webfetch_payload,
)


def webfetch_payload(content: list[dict]) -> dict:
    return {
        "content": content,
        "usage": {
            "input_tokens": 120,
            "output_tokens": 8,
            "server_tool_use": {"web_fetch_requests": 1},
        },
    }


def test_page_text_comes_from_the_tool_result_not_the_model():
    payload = webfetch_payload(
        [
            {"type": "text", "text": "Here is a summary the model made up."},
            {
                "type": "web_fetch_tool_result",
                "content": {
                    "type": "web_fetch_result",
                    "url": "https://docs.example.com/oauth",
                    "content": {
                        "type": "document",
                        "title": "OAuth",
                        "source": {
                            "type": "text",
                            "media_type": "text/plain",
                            "data": "Register an app to get a client ID.",
                        },
                    },
                },
            },
        ]
    )
    result = parse_webfetch_payload(payload, "https://docs.example.com/oauth", "m")
    assert result.markdown == "Register an app to get a client ID."
    assert "summary the model made up" not in (result.markdown or "")
    assert result.usage["web_fetch_requests"] == 1
    assert result.ok


def test_webfetch_error_code_is_surfaced():
    payload = webfetch_payload(
        [
            {
                "type": "web_fetch_tool_result",
                "content": {
                    "type": "web_fetch_tool_result_error",
                    "error_code": "url_not_accessible",
                },
            }
        ]
    )
    result = parse_webfetch_payload(payload, "https://x.example/a", "m")
    assert result.error_kind == "url_not_accessible"
    assert not result.ok


def test_pdf_is_not_mistaken_for_page_text():
    payload = webfetch_payload(
        [
            {
                "type": "web_fetch_tool_result",
                "content": {
                    "type": "web_fetch_result",
                    "content": {
                        "type": "document",
                        "source": {
                            "type": "base64",
                            "media_type": "application/pdf",
                            "data": "JVBER",
                        },
                    },
                },
            }
        ]
    )
    result = parse_webfetch_payload(payload, "https://x.example/a.pdf", "m")
    assert result.error_kind == "unsupported_content_type"


@pytest.mark.parametrize(
    "exc,expected",
    [
        (firecrawl.RateLimitError("slow down"), "rate_limit"),
        (firecrawl.PaymentRequiredError("out of credits"), "credits"),
        (firecrawl.RequestTimeoutError("timed out"), "timeout"),
        (firecrawl.BadRequestError("bad url"), "bad_request"),
        (firecrawl.InternalServerError("boom"), "unavailable"),
        (Exception("Unauthorized: Invalid token"), "invalid_key"),
        (Exception("something else"), "other"),
    ],
)
def test_firecrawl_errors_are_classified(exc, expected):
    assert _classify(exc) == expected


@pytest.mark.parametrize(
    "status,markdown,expected",
    [
        (403, "", "HTTP 403"),
        (200, "Sign in to continue", "short page mentioning 'sign in'"),
        (200, "Create an OAuth app. " * 80, None),
        (200, "", None),
    ],
)
def test_gate_detection(status, markdown, expected):
    result = FetchResult(url="u", source="firecrawl", status=status, markdown=markdown)
    assert looks_like_gate(result) == expected
