from dataclasses import dataclass
from typing import Literal

MessageRole = Literal["system", "user", "assistant"]


@dataclass
class Message:
    role: MessageRole
    content: str


@dataclass
class Conversation:
    messages: list[Message]

    def latest_user_message(self) -> Message | None:
        for message in reversed(self.messages):
            if message.role == "user":
                return message

        return None


conversation = Conversation(
    messages=[
        Message("system", "You are helpful."),
        Message("user", "What is an AI agent?"),
        Message("assistant", "An agent can use tools."),
        Message("user", "What is RAG?"),
    ]
)

latest = conversation.latest_user_message()

if latest is None:
    print("No user message found.")
else:
    print(f"Latest question: {latest.content}")