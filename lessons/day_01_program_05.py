def add_conversation_message(
    role: str,
    content: str,
    history: list[dict[str, str]] | None = None,
) -> list[dict[str, str]]:
    if role not in ("user", "assistant"):
        raise ValueError("Role must be 'user' or 'assistant'.")

    cleaned_content = content.strip()

    if not cleaned_content:
        raise ValueError("Content cannot be empty.")

    if history is None:
        history = []

    history.append(
        {
            "role": role,
            "content": cleaned_content,
        }
    )

    return history


conversation = add_conversation_message("user", "What is Python?")
conversation = add_conversation_message(
    "assistant",
    "Python is a readable, general-purpose programming language.",
    conversation,
)

for message in conversation:
    print(f"{message['role'].title()}: {message['content']}")