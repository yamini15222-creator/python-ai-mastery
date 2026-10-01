from typing import Any


def build_ai_request(
    prompt: str,
    model: str = "gpt-5",
    temperature: float = 0.7,
    max_tokens: int = 300,
) -> dict[str, Any]:
    cleaned_prompt = prompt.strip()

    if not cleaned_prompt:
        raise ValueError("Prompt cannot be empty.")

    if not 0 <= temperature <= 2:
        raise ValueError("Temperature must be between 0 and 2.")

    if max_tokens <= 0:
        raise ValueError("max_tokens must be greater than 0.")

    return {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": cleaned_prompt,
            }
        ],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }


request = build_ai_request(
    prompt=" Explain Python lists with an AI example. ",
    temperature=0.5,
    max_tokens=250,
)

print(request)
print(request["messages"][0]["content"])
#with challenge
from typing import Any


def build_ai_request(
    prompt: str,
    model: str = "gpt-5",
    temperature: float = 0.7,
    max_tokens: int = 300,
) -> dict[str, Any]:
    cleaned_prompt = prompt.strip()

    if not cleaned_prompt:
        raise ValueError("Prompt cannot be empty.")

    if not 0 <= temperature <= 2:
        raise ValueError("Temperature must be between 0 and 2.")

    if max_tokens <= 0:
        raise ValueError("max_tokens must be greater than 0.")

    return {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": cleaned_prompt,
            }
        ],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }


def add_conversation_message(
    role: str,
    content: str,
    history: list[dict[str, str]] | None = None,
) -> list[dict[str, str]]:
    if role not in ("user", "assistant"):
        raise ValueError("role must be 'user' or 'assistant'.")

    cleaned_content = content.strip()

    if not cleaned_content:
        raise ValueError("content must be a non-empty string.")

    if history is None:
        history = []

    history.append(
        {
            "role": role,
            "content": cleaned_content,
        }
    )

    return history


request = build_ai_request(
    prompt=" Explain Python lists with an AI example. ",
    temperature=0.5,
    max_tokens=250,
)

print(request)
print(request["messages"][0]["content"])


conversation = add_conversation_message(
    role="user",
    content="Hello, explain Python lists.",
)

conversation = add_conversation_message(
    role="assistant",
    content="A Python list stores multiple values in one variable.",
    history=conversation,
)

print(conversation)