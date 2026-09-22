"""
Optional: transcribes audio files to text using Whisper (or similar) API.
"""

from app.config import WHISPER_API_KEY, ENABLE_AUDIO_INPUT


def transcribe_audio(audio_path: str) -> str:
    if not ENABLE_AUDIO_INPUT:
        raise RuntimeError("Audio input is disabled. Set ENABLE_AUDIO_INPUT=true in .env.")

    if not WHISPER_API_KEY:
        raise RuntimeError("WHISPER_API_KEY is not set.")

    # TODO: implement actual Whisper API call
    # Example (pseudocode):
    # response = whisper_client.transcribe(audio_path)
    # return response.text

    raise NotImplementedError("Whisper transcription not yet implemented.")