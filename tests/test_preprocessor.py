import pytest
from app.ingestion.preprocessor import remove_filler_words, normalize_whitespace, preprocess, chunk_transcript


def test_remove_filler_words():
    text = "So, um, I think we should, like, ship this Friday."
    result = remove_filler_words(text)
    assert "um" not in result.lower()
    assert "like" not in result.lower()
    assert "ship this Friday" in result


def test_normalize_whitespace():
    text = "Line one.\n\n\n\nLine two."
    result = normalize_whitespace(text)
    assert "\n\n\n" not in result


def test_preprocess_combines_cleaning():
    text = "Um, so, like, this is a test.\n\n\n\nSecond line."
    result = preprocess(text)
    assert "um" not in result.lower()
    assert "\n\n\n" not in result


def test_chunk_transcript_respects_max_chars():
    text = "Paragraph one.\n\n" * 200
    chunks = chunk_transcript(text, max_chars=500)
    assert all(len(chunk) <= 500 + 50 for chunk in chunks)  # small buffer for boundaries
    assert len(chunks) > 1


def test_chunk_transcript_single_chunk_for_short_text():
    text = "Just one short paragraph."
    chunks = chunk_transcript(text, max_chars=8000)
    assert len(chunks) == 1
    assert chunks[0] == text