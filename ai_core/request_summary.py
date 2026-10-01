from typing import Any


def summarize_request(request: dict[str, Any]) -> str:
    messages = request.get("messages", [])
    model = request.get("model", "unknown")
    temperature = request.get("temperature", "unknown")
    max_tokens = request.get("max_tokens", "unknown")

    return (
        f"Model: {model}\n"
        f"Temperature: {temperature}\n"
        f"Max tokens: {max_tokens}\n"
        f"Message count: {len(messages)}"
    )