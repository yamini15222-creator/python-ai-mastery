import pytest

from ai_core.message_tools import InvalidMessageError, create_message


def test_create_message_returns_clean_message() -> None:
    message = create_message("user", "  What is RAG?  ")

    assert message == {
        "role": "user",
        "content": "What is RAG?",
    }


@pytest.mark.parametrize("role", ["admin", "", "bot"])
def test_create_message_rejects_invalid_role(role: str) -> None:
    with pytest.raises(InvalidMessageError, match="Role is invalid"):
        create_message(role, "Hello")