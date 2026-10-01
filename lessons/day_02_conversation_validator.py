VALID_ROLES = {"system", "user", "assistant"}


def validate_message(message: dict[str, str]) -> str | None:
    role = message.get("role", "")
    content = message.get("content", "").strip()

    if role not in VALID_ROLES:
        return f"Invalid role: {role!r}"

    if not content:
        return "Message content cannot be empty."

    if len(content) > 500:
        return "Message content is too long for this demo."

    return None


def clean_conversation(
    conversation: list[dict[str, str]],
) -> list[dict[str, str]]:
    valid_messages: list[dict[str, str]] = []

    for message in conversation:
        error = validate_message(message)

        if error:
            print(f"Skipped message: {error}")
            continue

        valid_messages.append(
            {
                "role": message["role"],
                "content": message["content"].strip(),
            }
        )

    return valid_messages


def count_messages_by_role(
    conversation: list[dict[str, str]],
) -> dict[str, int]:
    counts: dict[str, int] = {}

    for message in conversation:
        role = message["role"]
        counts[role] = counts.get(role, 0) + 1

    return counts


conversation = [
    {"role": "system", "content": " You are a helpful Python tutor. "},
    {"role": "user", "content": " What is an AI agent? "},
    {"role": "unknown", "content": "This should be rejected."},
    {"role": "assistant", "content": "   "},
    {"role": "assistant", "content": "An AI agent can reason and use tools."},
]

cleaned_conversation = clean_conversation(conversation)

print("\nValid conversation:")
for index, message in enumerate(cleaned_conversation, start=1):
    print(f"{index}. {message['role'].title()}: {message['content']}")

role_counts = count_messages_by_role(cleaned_conversation)

print("\nMessage counts by role:")
print(role_counts)