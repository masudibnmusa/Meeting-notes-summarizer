#!/bin/bash
# Entry point script for the Meeting Notes Summarizer

set -e

if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Run: python -m venv venv"
    exit 1
fi

source venv/bin/activate

if [ -z "$1" ]; then
    echo "Usage: ./run.sh <path-to-transcript> [output-format]"
    echo "  output-format: markdown | json | email | slack (default: markdown)"
    exit 1
fi

TRANSCRIPT_PATH=$1
FORMAT=${2:-markdown}

python -m app.main --transcript "$TRANSCRIPT_PATH" --format "$FORMAT"
```

**`data/transcripts/.gitkeep`**
```
```
(empty file, just keeps the folder in git)

**`data/summaries/.gitkeep`**
```
```

**`data/logs/.gitkeep`**
```