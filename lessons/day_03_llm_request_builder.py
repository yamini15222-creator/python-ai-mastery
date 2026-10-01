from typing import Any

VALID_ROLES = {"system", "user", "assistant"}


def validate_message(role: str, content: str) -> dict[str, str]:
    cleaned_content = content.strip()

    if role not in VALID_ROLES:
        raise ValueError(f"Invalid role: {role!r}")

    if not cleaned_content:
        raise ValueError("Message content cannot be empty.")

    return {
        "role": role,
        "content": cleaned_content,
    }


def create_llm_request(
    system_instruction: str,
    user_prompt: str,
    *,
    model: str = "gpt-5",
    temperature: float = 0.7,
    max_tokens: int = 500,
) -> dict[str, Any]:
    if not 0 <= temperature <= 2:
        raise ValueError("Temperature must be between 0 and 2.")

    if max_tokens <= 0:
        raise ValueError("max_tokens must be greater than 0.")

    system_message = validate_message("system", system_instruction)
    user_message = validate_message("user", user_prompt)

    return {
        "model": model,
        "messages": [system_message, user_message],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }


def estimate_request_size(request: dict[str, Any]) -> int:
    total = 0

    for message in request.get("messages", []):
        content = message.get("content", "")
        total += len(content)

    return total


request = create_llm_request(
    system_instruction="You are a helpful Python and AI tutor.",
    user_prompt="Explain RAG with a simple example.",
    model="gpt-5",
    temperature=0.4,
    max_tokens=300,
)

print("LLM request created successfully:\n")

for key, value in request.items():
    print(f"{key}: {value}")

request_size = estimate_request_size(request)

print(f"\nTotal message content size: {request_size} characters")