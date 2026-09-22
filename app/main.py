"""
Entry point for the Meeting Notes Summarizer.
Supports CLI usage for now; can be extended to Streamlit or an API later.
"""

import argparse
from app.ingestion.transcript_loader import load_transcript
from app.ingestion.preprocessor import preprocess
from app.extraction.summarizer import generate_summary
from app.extraction.action_item_extractor import extract_action_items
from app.extraction.decision_extractor import extract_decisions
from app.output.formatter import format_output


def run(transcript_path: str, output_format: str = "markdown"):
    raw_text = load_transcript(transcript_path)
    clean_text = preprocess(raw_text)

    summary = generate_summary(clean_text)
    action_items = extract_action_items(clean_text)
    decisions = extract_decisions(clean_text)

    result = format_output(
        summary=summary,
        action_items=action_items,
        decisions=decisions,
        output_format=output_format,
    )

    print(result)
    return result


def main():
    parser = argparse.ArgumentParser(description="Meeting Notes Summarizer")
    parser.add_argument("--transcript", required=True, help="Path to transcript file")
    parser.add_argument(
        "--format",
        default="markdown",
        choices=["markdown", "json", "email", "slack"],
        help="Output format",
    )
    args = parser.parse_args()
    run(args.transcript, args.format)


if __name__ == "__main__":
    main()