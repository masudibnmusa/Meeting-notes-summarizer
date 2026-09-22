"""
Validates extracted action items to catch malformed or incomplete entries.
"""


def validate_action_items(items: list[dict]) -> list[dict]:
    """
    Keep only well-formed action items: must have a non-empty 'task'.
    Fills missing owner/deadline with None rather than dropping the item.
    """
    valid = []
    for item in items:
        if not isinstance(item, dict):
            continue
        task = item.get("task", "").strip() if item.get("task") else ""
        if not task:
            continue
        valid.append({
            "task": task,
            "owner": item.get("owner") or None,
            "deadline": item.get("deadline") or None,
        })
    return valid