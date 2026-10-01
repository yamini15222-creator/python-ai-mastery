def find_first_user_question(
    conversation: list[dict[str, str]],
) -> str | None:
    for message in conversation:
        if message.get("role") == "user":
            return message.get("content", "").strip()

    return None


conversation = [
    {"role": "system", "content": "You are helpful."},
    {"role": "assistant", "content": "Hello!"},
    {"role": "user", "content": "How does an LLM work?"},
    {"role": "user", "content": "What is an embedding?"},
]

question = find_first_user_question(conversation)

if question is None:
    print("No user question found.")
else:
    print(f"First question: {question}")