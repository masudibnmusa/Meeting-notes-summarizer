"""
Pushes extracted action items to a task tracker (Asana/Jira/Trello) via API.
"""

from app.config import ASANA_API_KEY, JIRA_API_KEY


def export_to_asana(action_items: list[dict], project_id: str):
    if not ASANA_API_KEY:
        raise RuntimeError("ASANA_API_KEY is not set.")
    # TODO: implement Asana API call per action item
    raise NotImplementedError("Asana export not yet implemented.")


def export_to_jira(action_items: list[dict], project_key: str):
    if not JIRA_API_KEY:
        raise RuntimeError("JIRA_API_KEY is not set.")
    # TODO: implement Jira API call per action item
    raise NotImplementedError("Jira export not yet implemented.")