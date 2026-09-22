"""
Formats the meeting summary as an email-ready message.
"""


def format_email(summary: str, action_items: list[dict], decisions: list[str]) -> str:
    lines = [
        "Subject: Meeting Summary\n",
        "Hi all,\n",
        "Here's a summary of our meeting:\n",
        summary,
        "\nDecisions made:",
    ]
    lines += [f"  - {d}" for d in decisions] if decisions else ["  - None"]

    lines.append("\nAction items:")
    if action_items:
        for item in action_items:
            owner = item.get("owner") or "Unassigned"
            deadline = item.get("deadline") or "No deadline"
            lines.append(f"  - {item.get('task')} ({owner}, due {deadline})")
    else:
        lines.append("  - None")

    lines.append("\nBest,\nMeeting Notes Summarizer")
    return "\n".join(lines)