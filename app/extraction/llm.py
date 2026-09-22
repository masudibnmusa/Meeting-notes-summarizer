"""
Wrapper around the LLM API (Claude/GPT) used for all extraction calls.
"""

from app.config import LLM_PROVIDER, LLM_MODEL, LLM_API_KEY


def call_llm(prompt: str, max_tokens: int = 1000) -> str:
    if LLM_PROVIDER == "anthropic":
        return _call_anthropic(prompt, max_tokens)
    elif LLM_PROVIDER == "openai":
        return _call_openai(prompt, max_tokens)
    else:
        raise ValueError(f"Unsupported LLM_PROVIDER: {LLM_PROVIDER}")


def _call_anthropic(prompt: str, max_tokens: int) -> str:
    import anthropic

    client = anthropic.Anthropic(api_key=LLM_API_KEY)
    response = client.messages.create(
        model=LLM_MODEL,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text


def _call_openai(prompt: str, max_tokens: int) -> str:
    import openai

    client = openai.OpenAI(api_key=LLM_API_KEY)
    response = client.chat.completions.create(
        model=LLM_MODEL,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content