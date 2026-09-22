"""
Loads a transcript from a text file (or plain string) into memory.
"""

from pathlib import Path


def load_transcript(source: str) -> str:
    """
    Load transcript text from a file path or return the string directly
    if it doesn't point to an existing file.
    """
    path = Path(source)
    if path.exists() and path.is_file():
        return path.read_text(encoding="utf-8")
    return source  # treat as raw pasted text