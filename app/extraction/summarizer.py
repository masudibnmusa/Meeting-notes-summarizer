"""
Generates a concise overview of the meeting using the LLM.
"""

from app.extraction.llm import call_llm
from app.extraction.prompt_templates import SUMMARY_PROMPT


def generate_summary(transcript_text: str) -> str:
    prompt = SUMMARY_PROMPT.format(transcript=transcript_text)
    response = call_llm(prompt)
    return response.strip()