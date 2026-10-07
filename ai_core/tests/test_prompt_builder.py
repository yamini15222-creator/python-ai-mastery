import pytest

from ai_core.prompt_builder import (
    build_ai_request,
    validate_level,
    validate_topic,
)


def test_valid_topic() -> None:
    assert validate_topic("Python") == "Python"


def test_topic_is_trimmed() -> None:
    assert validate_topic("  Python  ") == "Python"


def test_empty_topic_fails() -> None:
    with pytest.raises(ValueError):
        validate_topic("")


def test_invalid_level_fails() -> None:
    with pytest.raises(ValueError):
        validate_level("expert")


def test_valid_request() -> None:
    request = build_ai_request(
        "NumPy",
        "beginner",
    )

    assert request["topic"] == "NumPy"
    assert request["level"] == "beginner"
    assert "NumPy" in request["prompt"]