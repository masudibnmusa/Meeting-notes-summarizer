"""
Extracts action items (task, owner, deadline) from the transcript.
"""

import json
from app.extraction.llm import call_llm
from app.extraction.prompt_templates import ACTION_ITEMS_PROMPT
from app.utils.validators import validate_action_items


def extract_action_items(transcript_text: str) -> list[dict]:
    prompt = ACTION_ITEMS_PROMPT.format(transcript=transcript_text)
    response = call_llm(prompt)

    try:
        items = json.loads(response)
    except json.JSONDecodeError:
        items = []

    return validate_action_items(items)