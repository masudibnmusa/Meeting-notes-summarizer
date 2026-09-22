"""
Optional: posts the formatted summary to a Slack channel.
"""

from app.config import SLACK_BOT_TOKEN, SLACK_CHANNEL


def post_to_slack(message: str):
    if not SLACK_BOT_TOKEN:
        raise RuntimeError("SLACK_BOT_TOKEN is not set.")

    # TODO: implement via slack_sdk
    # from slack_sdk import WebClient
    # client = WebClient(token=SLACK_BOT_TOKEN)
    # client.chat_postMessage(channel=SLACK_CHANNEL, text=message)

    raise NotImplementedError("Slack delivery not yet implemented.")