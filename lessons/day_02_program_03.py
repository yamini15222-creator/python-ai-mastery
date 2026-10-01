def count_messages_by_role(
    conversation: list[dict[str, str]],
) -> dict[str, int]:
    counts: dict[str, int] = {
        "system": 0,
        "user": 0,
        "assistant": 0,
    }

    for message in conversation:
        role = message.get("role")

        if role in counts:
            counts[role] += 1

    return counts


conversation = [
    {"role": "system", "content": "You are a helpful AI tutor."},
    {"role": "user", "content": "What is Python?"},
    {"role": "assistant", "content": "Python is a programming language."},
    {"role": "user", "content": "What is RAG?"},
]

print(count_messages_by_role(conversation))