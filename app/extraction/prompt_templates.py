"""
Prompt templates for each extraction task.
Keep these versioned and easy to tune independently.
"""

SUMMARY_PROMPT = """You are summarizing a meeting transcript.
Write a concise overview (3-6 sentences) of what was discussed.
Do not include action items or decisions here — just the general discussion.

Transcript:
{transcript}

Summary:"""


ACTION_ITEMS_PROMPT = """Extract all action items from this meeting transcript.
For each action item, include: task, owner (if stated), and deadline (if stated).
Only include items that are explicitly stated or clearly implied — do not invent owners or deadlines.
Respond ONLY with a JSON array, no other text. Format:
[{{"task": "...", "owner": "...", "deadline": "..."}}]

Transcript:
{transcript}

JSON:"""


DECISIONS_PROMPT = """Extract all explicit decisions or agreements made in this meeting transcript.
Only include decisions that were clearly agreed upon, not open discussion points.
Respond ONLY with a JSON array of strings, no other text. Format:
["Decision 1", "Decision 2"]

Transcript:
{transcript}

JSON:"""