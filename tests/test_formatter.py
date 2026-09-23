import json
import pytest
from app.output.formatter import format_output


def test_format_output_markdown():
    result = format_output(
        summary="We discussed the roadmap.",
        action_items=[{"task": "Send report", "owner": "Sarah", "deadline": "Friday"}],
        decisions=["Launch delayed to next quarter."],
        output_format="markdown",
    )
    assert "## Meeting Summary" in result
    assert "We discussed the roadmap." in result
    assert "Send report" in result
    assert "Launch delayed to next quarter." in result


def test_format_output_json():
    result = format_output(
        summary="Summary text.",
        action_items=[],
        decisions=[],
        output_format="json",
    )
    parsed = json.loads(result)
    assert parsed["summary"] == "Summary text."
    assert parsed["action_items"] == []
    assert parsed["decisions"] == []


def test_format_output_email():
    result = format_output(
        summary="Summary text.",
        action_items=[{"task": "Do X", "owner": "Bob", "deadline": "Monday"}],
        decisions=[],
        output_format="email",
    )
    assert "Subject:" in result
    assert "Do X" in result


def test_format_output_slack():
    result = format_output(
        summary="Summary text.",
        action_items=[],
        decisions=["Decision A"],
        output_format="slack",
    )
    assert "*Meeting Summary*" in result
    assert "Decision A" in result