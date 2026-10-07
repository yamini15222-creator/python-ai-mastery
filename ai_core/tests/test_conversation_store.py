import json
from pathlib import Path


class ConversationStore:
    """Persist and load conversation history using JSON."""

    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path

    def save(self, history: list[dict[str, str]]) -> None:
        """Save conversation history to a JSON file."""
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(
                history,
                file,
                indent=4,
                ensure_ascii=False,
            )

    def load(self) -> list[dict[str, str]]:
        """Load conversation history from a JSON file."""
        if not self.file_path.exists():
            return []

        with self.file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise TypeError(
                "Conversation history must be a JSON list."
            )

        return data