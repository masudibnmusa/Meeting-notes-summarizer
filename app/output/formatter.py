"""
Combines summary, decisions, and action items into a single structured
result, then delegates to a destination-specific formatter if requested.
"""

from app.output.email_formatter import format_email
from app.output.slack_formatter import format_slack


def format_output(summary: str, action_items: list[dict], decisions: list[str], output_format: str = "markdown") -> str:
    if output_format == "json":
        import json
        return json.dumps(
            {"summary": summary, "decisions": decisions, "action_items": action_items},
            indent=2,
        )

    if output_format == "email":
        return format_email(summary, action_items, decisions)

    if output_format == "slack":
        return format_slack(summary, action_items, decisions)

    # default: markdown
    return _format_markdown(summary, action_items, decisions)


def _format_markdown(summary: str, action_items: list[dict], decisions: list[str]) -> str:
    lines = ["## Meeting Summary\n", summary, "\n## Decisions\n"]
    lines += [f"- {d}" for d in decisions] if decisions else ["- None recorded"]

    lines.append("\n## Action Items\n")
    if action_items:
        for item in action_items:
            owner = item.get("owner") or "Unassigned"
            deadline = item.get("deadline") or "No deadline"
            lines.append(f"- **{item.get('task')}** — {owner} (Due: {deadline})")
    else:
        lines.append("- None recorded")

    return "\n".join(lines)