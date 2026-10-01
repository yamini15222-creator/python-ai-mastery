import logging
from typing import Any

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)

logger = logging.getLogger(__name__)

VALID_ROLES = {"system", "user", "assistant"}

class InvalidAIRequestError(ValueError):
    """Raised when an AI request contains invalid data."""

def validate_messages(messages: list[dict[str, Any]]) -> None:
    """Validate the messages sent to the AI."""

    if not isinstance(messages, list):
        raise InvalidAIRequestError("messages must be a list")

    if not messages:
        raise InvalidAIRequestError("messages cannot be empty")

    for index, message in enumerate(messages):
        if not isinstance(message, dict):
            raise InvalidAIRequestError(
                f"Message at index {index} must be a dictionary"
            )

        if "role" not in message:
            raise InvalidAIRequestError(
                f"Message at index {index} is missing 'role'"
            )

        if "content" not in message:
            raise InvalidAIRequestError(
                f"Message at index {index} is missing 'content'"
            )

        role = message["role"]
        content = message["content"]

        if role not in VALID_ROLES:
            raise InvalidAIRequestError(
                f"Invalid role '{role}'. "
                f"Allowed roles: {', '.join(sorted(VALID_ROLES))}"
            )

        if not isinstance(content, str):
            raise InvalidAIRequestError(
                f"Content at index {index} must be a string"
            )

        if not content.strip():
            raise InvalidAIRequestError(
                f"Content at index {index} cannot be empty"
            )


def validate_max_tokens(max_tokens: int) -> None:
    """Validate the max_tokens value."""

    if isinstance(max_tokens, bool) or not isinstance(max_tokens, int):
        raise InvalidAIRequestError(
            "max_tokens must be an integer"
        )

    if max_tokens <= 0:
        raise InvalidAIRequestError(
            "max_tokens must be greater than 0"
        )

    if max_tokens > 4000:
        raise InvalidAIRequestError(
            "max_tokens must not exceed 4000"
        )

def build_ai_request(
    messages: list[dict[str, Any]],
    max_tokens: int = 1000,
) -> dict[str, Any]:
    """Build and validate an AI request."""

    logger.info("Building AI request")

    validate_messages(messages)
    validate_max_tokens(max_tokens)

    request = {
        "messages": messages,
        "max_tokens": max_tokens,
    }

    logger.info("AI request created successfully")

    return request

def main() -> None:
    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant.",
        },
        {
            "role": "user",
            "content": "Explain Python exception handling.",
        },
    ]

    try:
        request = build_ai_request(
            messages=messages,
            max_tokens=1000,
        )

        print("Valid request:")
        print(request)

    except InvalidAIRequestError as error:
        logger.error("Invalid AI request: %s", error)


if __name__ == "__main__":
    main()