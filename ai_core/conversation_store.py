
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
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
        self.content = self.content.strip()

        if not self.content:
            raise ValueError("Message content cannot be empty.")




@dataclass
class AgentState:
    name: str
    messages: list[ChatMessage] = field(default_factory=list)
    tools_used: list[str] = field(default_factory=list)

    def add_message(
        self,
        role: MessageRole,
        content: str,
    ) -> ChatMessage:
        message = ChatMessage(
            role=role,
            content=content,
        )

        self.messages.append(message)
        return message

    def record_tool_use(self, tool_name: str) -> None:
        cleaned_tool_name = tool_name.strip()

        if not cleaned_tool_name:
            raise ValueError("Tool name cannot be empty.")

        self.tools_used.append(cleaned_tool_name)

    def latest_user_message(self) -> ChatMessage | None:
        for message in reversed(self.messages):
            if message.role == "user":
                return message

        return None

    def clear_conversation(self) -> None:
        self.messages.clear()

    def summary(self) -> str:
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




def save_recent_messages(
    agent: AgentState,
    file_path: Path,
    limit: int,
) -> None:

    if limit < 0:
        raise ValueError("Limit cannot be negative.")

    
    recent_messages = agent.messages[-limit:] if limit > 0 else []

    
    data = []

    for message in recent_messages:
        data.append(
            {
                "role": message.role,
                "content": message.content,
                "created_at": message.created_at.isoformat(),
            }
        )

    # Save the data to JSON
    with file_path.open("w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4,
        )


agent = AgentState(name="Python AI Tutor")


agent.add_message("user", "What is Python?")
agent.add_message("assistant", "Python is a programming language.")

agent.add_message("user", "What is a variable?")
agent.add_message("assistant", "A variable stores a value.")

agent.add_message("user", "What is a list?")
agent.add_message("assistant", "A list stores multiple values.")

agent.add_message("user", "What is a tuple?")
agent.add_message("assistant", "A tuple is an immutable collection.")

agent.add_message("user", "What is a dictionary?")
agent.add_message(
    "assistant",
    "A dictionary stores key-value pairs.",
)


print("Total messages:", len(agent.messages))


file_path = Path("recent_messages.json")

save_recent_messages(
    agent=agent,
    file_path=file_path,
    limit=3,
)


print(f"Saved recent messages to: {file_path}")


with file_path.open("r", encoding="utf-8") as file:
    saved_messages = json.load(file)

print("\nSaved messages:")
print(json.dumps(saved_messages, indent=4))

