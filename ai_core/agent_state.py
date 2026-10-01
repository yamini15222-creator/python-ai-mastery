
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Literal

MessageRole = Literal["system", "user", "assistant"]


@dataclass
class ChatMessage:
    role: MessageRole
    content: str
    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    def __post_init__(self) -> None:
        # Remove unnecessary spaces
        self.content = self.content.strip()

        # Prevent empty messages
        if not self.content:
            raise ValueError("Message content cannot be empty.")


@dataclass
class AgentState:
    name: str
    messages: list[ChatMessage] = field(default_factory=list)
    tools_used: list[str] = field(default_factory=list)

    def add_message(self, role: MessageRole, content: str) -> ChatMessage:
        """Add a new message to the conversation."""
        message = ChatMessage(role=role, content=content)
        self.messages.append(message)
        return message

    def record_tool_use(self, tool_name: str) -> None:
        """Record a tool used by the agent."""
        cleaned_tool_name = tool_name.strip()

        if not cleaned_tool_name:
            raise ValueError("Tool name cannot be empty.")

        self.tools_used.append(cleaned_tool_name)

    def latest_user_message(self) -> ChatMessage | None:
        """Return the latest user message."""
        for message in reversed(self.messages):
            if message.role == "user":
                return message

        return None

    def clear_conversation(self) -> None:
        """Remove all conversation messages while preserving agent information."""
        self.messages.clear()

    def summary(self) -> str:
        """Return a summary of the current agent state."""
        latest_message = self.latest_user_message()

        if latest_message is None:
            latest_question = "No user question yet."
        else:
            latest_question = latest_message.content

        return (
            f"Agent: {self.name}\n"
            f"Messages: {len(self.messages)}\n"
            f"Tools used: {self.tools_used or ['None']}\n"
            f"Latest user message: {latest_question}"
        )


agent = AgentState(name="Python AI Tutor")


agent.add_message(
    "system",
    "You are a helpful Python and AI tutor.",
)



agent.add_message(
    "user",
    "Explain the difference between RAG and fine-tuning.",
)



agent.record_tool_use("knowledge_search")

print("----- BEFORE CLEARING -----")
print(agent.summary())

agent.clear_conversation()

print("\n----- AFTER CLEARING -----")
print(agent.summary())


print("\n----- VERIFICATION -----")
print("Name:", agent.name)
print("Messages:", agent.messages)
print("Tools used:", agent.tools_used)

