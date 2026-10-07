from dataclasses import dataclass, field


@dataclass
class AgentState:
    """Maintain the current learning-assistant state."""

    topic: str = ""
    level: str = ""
    history: list[dict[str, str]] = field(default_factory=list)

    def add_message(self, role: str, content: str) -> None:
        """Add a message to conversation history."""
        self.history.append(
            {
                "role": role,
                "content": content,
            }
        )