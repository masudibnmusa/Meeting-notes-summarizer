import pytest
from unittest.mock import patch
from app.extraction.summarizer import generate_summary


@patch("app.extraction.summarizer.call_llm")
def test_generate_summary_returns_stripped_text(mock_call_llm):
    mock_call_llm.return_value = "  This is the meeting summary.  \n"
    result = generate_summary("Some transcript text.")
    assert result == "This is the meeting summary."
    mock_call_llm.assert_called_once()


@patch("app.extraction.summarizer.call_llm")
def test_generate_summary_passes_transcript_into_prompt(mock_call_llm):
    mock_call_llm.return_value = "Summary."
    transcript = "Alice: We should launch next week."
    generate_summary(transcript)
    called_prompt = mock_call_llm.call_args[0][0]
    assert transcript in called_prompt