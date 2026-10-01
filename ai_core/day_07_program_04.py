import json
from pathlib import Path


def save_recent_messages(
    messages: list[dict[str, str]],
    file_path: Path,
    limit: int,
) -> None:
    if limit <= 0:
        raise ValueError("limit must be greater than zero.")

    file_path.parent.mkdir(parents=True, exist_ok=True)

    recent_messages = messages[-limit:]

    with file_path.open("w", encoding="utf-8") as file:
        json.dump(recent_messages, file, indent=2)


conversation = [
    {"role": "system", "content": "You are helpful."},
    {"role": "user", "content": "What is Python?"},
    {"role": "assistant", "content": "Python is a programming language."},
    {"role": "user", "content": "What is RAG?"},
    {"role": "assistant", "content": "RAG retrieves relevant knowledge first."},
]

memory_file = Path("data") / "recent_messages.json"

save_recent_messages(conversation, memory_file, limit=3)

print(memory_file.read_text(encoding="utf-8"))