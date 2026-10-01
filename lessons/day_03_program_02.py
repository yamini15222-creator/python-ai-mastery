from typing import Any


def estimate_request_size(request: dict[str, Any]) -> int:
    total_characters = 0

    for message in request.get("messages", []):
        content = message.get("content", "")
        total_characters += len(content)

    return total_characters


request = {
    "model": "gpt-5",
    "messages": [
        {"role": "system", "content": "You are a helpful tutor."},
        {"role": "user", "content": "Explain RAG simply."},
    ],
}

print(f"Total characters: {estimate_request_size(request)}")