# Meeting Notes Summarizer

Turn a raw meeting transcript into a structured summary — key discussion points, decisions made, and action items with owners and deadlines. Supports optional speaker attribution and multiple export formats (email, Slack, Notion, task trackers).

## Overview

**Core idea:** Clean and chunk the transcript → extract structured info (summary, decisions, action items) via prompted LLM calls → format the output for different destinations (email, Notion, Slack, Jira/Asana).

## How It Works

1. **Input** — paste transcript, upload a text file, or upload audio (auto-transcribed via Whisper or similar)
2. **Preprocessing** — clean filler words, timestamps, speaker labels; chunk if the transcript is long
3. **Speaker/segment parsing** (optional) — identify who said what, if diarization data exists
4. **Summarization** — LLM generates a concise overview of what was discussed
5. **Action item extraction** — LLM identifies tasks, owners, and deadlines (e.g. "Sarah will send the report by Friday")
6. **Decision extraction** — LLM pulls out explicit decisions/agreements made
7. **Formatting & export** — structure output for email, Slack, Notion, or task management tools (Asana/Jira via API)
8. **Delivery** (optional) — auto-send the summary to attendees via email/Slack after the meeting

## 📁 Project Structure

```text
meeting-summarizer/
│
├── app/
│   ├── main.py                         # Entry point (Streamlit/CLI/API)
│   ├── config.py                       # API keys, model settings, output preferences
│   │
│   ├── ingestion/
│   │   ├── transcript_loader.py        # Load text/file input
│   │   ├── audio_transcriber.py       # Optional: Whisper API for audio → text
│   │   └── preprocessor.py             # Clean filler words, normalize formatting
│   │
│   ├── extraction/
│   │   ├── summarizer.py               # LLM: generate meeting overview
│   │   ├── action_item_extractor.py    # LLM: extract tasks, owners, deadlines
│   │   ├── decision_extractor.py       # LLM: extract key decisions/agreements
│   │   ├── prompt_templates.py         # Prompts for each extraction type
│   │   └── llm.py                      # Claude/GPT API wrapper
│   │
│   ├── output/
│   │   ├── formatter.py                # Structure results (JSON → readable formats)
│   │   ├── email_formatter.py          # Format as email-ready summary
│   │   ├── slack_formatter.py          # Format as Slack message
│   │   └── task_exporter.py            # Push tasks to Asana/Jira/Trello via API
│   │
│   ├── delivery/
│   │   ├── email_sender.py             # Optional: auto-send summary
│   │   └── slack_notifier.py           # Optional: post to Slack channel
│   │
│   └── utils/
│       └── validators.py               # Validate extracted action items
│
├── data/
│   ├── transcripts/                    # Raw uploaded transcripts/audio
│   ├── summaries/                      # Generated summaries (JSON/Markdown)
│   └── logs/                           # Application logs
│
├── tests/
│   ├── test_preprocessor.py
│   ├── test_summarizer.py
│   ├── test_action_item_extractor.py
│   └── test_formatter.py
│
├── .env                                # Environment variables
├── .env.example                        # Environment variable template
├── .gitignore
├── requirements.txt                    # Python dependencies
├── README.md
└── run.sh                              # Application startup script
```

## 🔄 Data Flow

```text
Transcript (text/audio)
        │
        ▼
transcript_loader.py / audio_transcriber.py
        │
        ▼
preprocessor.py
(Clean and normalize text)
        │
        ├──────────────────────┬──────────────────────┐
        ▼                      ▼                      ▼
summarizer.py        action_item_extractor.py   decision_extractor.py
        │                      │                      │
        └──────────────────────┴──────────────────────┘
                               │
                               ▼
                         formatter.py
                  (Combine into structured output)
                               │
             ┌─────────────────┼─────────────────┐
             ▼                 ▼                 ▼
   email_formatter.py  slack_formatter.py  task_exporter.py
             │                 │                 │
             └─────────────────┴─────────────────┘
                               │
                               ▼
                          delivery/
                    (Optional auto-delivery)
```


## Getting Started

### Prerequisites

- Python 3.10+
- An API key for your chosen LLM provider (Claude/GPT)
- (Optional) Whisper API access for audio transcription
- (Optional) API credentials for Slack, Notion, Asana, or Jira if using export/delivery features

### Installation

```bash
git clone <repo-url>
cd meeting-summarizer
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` with your API keys and settings.

### Usage

```bash
./run.sh
```

Or run directly:

```bash
python -m app.main --transcript path/to/transcript.txt
```

## Configuration

All API keys, model settings, and output preferences are managed via `.env` and read through `app/config.py`. See `.env.example` for the required variables.

## Known Limitations

- No deduplication/merge logic yet for action items or decisions extracted across chunks of long transcripts.
- Action item extraction can hallucinate owners/deadlines if not explicitly stated — treat extracted deadlines as suggestions, not verified facts.
- Speaker attribution quality depends on diarization data being available; without it, owner detection falls back to name mentions near a task.

## Testing

```bash
pytest tests/
```

## License

MIT