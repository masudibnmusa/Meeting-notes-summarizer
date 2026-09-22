"""
Extracts explicit decisions/agreements made during the meeting.
"""

import json
from app.extraction.llm import call_llm
from app.extraction.prompt_templates import DECISIONS_PROMPT


def extract_decisions(transcript_text: str) -> list[str]:
    prompt = DECISIONS_PROMPT.format(transcript=transcript_text)
    response = call_llm(prompt)

    try:
        decisions = json.loads(response)
    except json.JSONDecodeError:
        decisions = []

    return decisions