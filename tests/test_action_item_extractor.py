import json
import pytest
from unittest.mock import patch
from app.extraction.action_item_extractor import extract_action_items


@patch("app.extraction.action_item_extractor.call_llm")
def test_extract_action_items_parses_valid_json(mock_call_llm):
    mock_call_llm.return_value = json.dumps([
        {"task": "Send report", "owner": "Sarah", "deadline": "Friday"}
    ])
    result = extract_action_items("Some transcript.")
    assert len(result) == 1
    assert result[0]["task"] == "Send report"
    assert result[0]["owner"] == "Sarah"
    assert result[0]["deadline"] == "Friday"


@patch("app.extraction.action_item_extractor.call_llm")
def test_extract_action_items_handles_invalid_json(mock_call_llm):
    mock_call_llm.return_value = "not valid json"
    result = extract_action_items("Some transcript.")
    assert result == []


@patch("app.extraction.action_item_extractor.call_llm")
def test_extract_action_items_filters_malformed_entries(mock_call_llm):
    mock_call_llm.return_value = json.dumps([
        {"task": "", "owner": "Sarah", "deadline": "Friday"},
        {"task": "Valid task", "owner": None, "deadline": None},
    ])
    result = extract_action_items("Some transcript.")
    assert len(result) == 1
    assert result[0]["task"] == "Valid task"