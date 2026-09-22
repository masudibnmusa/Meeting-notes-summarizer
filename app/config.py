"""
Central configuration for the app.
Reads all values from environment variables — never hardcode secrets here.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# LLM settings
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "anthropic")  # "anthropic" or "openai"
LLM_MODEL = os.getenv("LLM_MODEL", "claude-sonnet-4-6")
LLM_API_KEY = os.getenv("LLM_API_KEY")

# Audio transcription
WHISPER_API_KEY = os.getenv("WHISPER_API_KEY")
ENABLE_AUDIO_INPUT = os.getenv("ENABLE_AUDIO_INPUT", "false").lower() == "true"

# Output preferences
DEFAULT_OUTPUT_FORMAT = os.getenv("DEFAULT_OUTPUT_FORMAT", "markdown")

# Integrations
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_CHANNEL = os.getenv("SLACK_CHANNEL")
ASANA_API_KEY = os.getenv("ASANA_API_KEY")
JIRA_API_KEY = os.getenv("JIRA_API_KEY")
NOTION_API_KEY = os.getenv("NOTION_API_KEY")

# Paths
DATA_DIR = os.getenv("DATA_DIR", "data")
TRANSCRIPTS_DIR = f"{DATA_DIR}/transcripts"
SUMMARIES_DIR = f"{DATA_DIR}/summaries"
LOGS_DIR = f"{DATA_DIR}/logs"