"""
Cleans raw transcript text: removes filler words, normalizes timestamps
and speaker labels, and chunks long transcripts.
"""

import re

FILLER_WORDS = ["um", "uh", "like", "you know", "sort of", "kind of"]


def remove_filler_words(text: str) -> str:
    for filler in FILLER_WORDS:
        text = re.sub(rf"\b{re.escape(filler)}\b", "", text, flags=re.IGNORECASE)
    return re.sub(r"\s+", " ", text).strip()


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def preprocess(raw_text: str) -> str:
    text = remove_filler_words(raw_text)
    text = normalize_whitespace(text)
    return text


def chunk_transcript(text: str, max_chars: int = 8000) -> list[str]:
    """
    Split a long transcript into chunks that fit within a reasonable
    LLM context size. Splits on paragraph boundaries where possible.
    """
    paragraphs = text.split("\n\n")
    chunks = []
    current = ""

    for para in paragraphs:
        if len(current) + len(para) + 2 <= max_chars:
            current += para + "\n\n"
        else:
            if current:
                chunks.append(current.strip())
            current = para + "\n\n"

    if current:
        chunks.append(current.strip())

    return chunks