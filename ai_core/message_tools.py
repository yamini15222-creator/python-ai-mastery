class InvalidMessageError(ValueError):
    """Raised when a message is invalid."""


def create_message(role: str, content: str) -> dict[str, str]:
    valid_roles = {"system", "user", "assistant"}
    cleaned_content = content.strip()

    if role not in valid_roles:
        raise InvalidMessageError("Role is invalid.")

    if not cleaned_content:
        raise InvalidMessageError("Content cannot be empty.")

    return {
        "role": role,
        "content": cleaned_content,
    }