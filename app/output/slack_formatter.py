"""
Formats the meeting summary as a Slack message (mrkdwn syntax).
"""


def format_slack(summary: str, action_items: list[dict], decisions: list[str]) -> str:
    lines = [":memo: *Meeting Summary*", summary, "\n*Decisions:*"]
    lines += [f"• {d}" for d in decisions] if decisions else ["• None"]

    lines.append("\n*Action Items:*")
    if action_items:
        for item in action_items:
            owner = item.get("owner") or "Unassigned"
            deadline = item.get("deadline") or "no deadline"
            lines.append(f"• *{item.get('task')}* — {owner} (due {deadline})")
    else:
        lines.append("• None")

    return "\n".join(lines)