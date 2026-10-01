import pytest

from ai_core.request_service import build_learning_request


def test_valid_request_has_expected_model_configuration():
    result = build_learning_request(
        topic="Python",
        level="beginner",
        model="gpt-4o-mini",
        temperature=0.7,
        max_tokens=500,
    )

    assert result["model"] == "gpt-4o-mini"
    assert result["temperature"] == 0.7
    assert result["max_tokens"] == 500


def test_valid_request_has_two_messages():
    result = build_learning_request(
        topic="Python",
        level="beginner",
    )

    assert len(result["messages"]) == 2


def test_empty_topic_raises_value_error():
    with pytest.raises(ValueError, match="topic cannot be empty"):
        build_learning_request(
            topic="",
            level="beginner",
        )


def test_invalid_temperature_raises_value_error():
    with pytest.raises(ValueError):
        build_learning_request(
            topic="Python",
            level="beginner",
            temperature=3.0,
        )


def test_empty_level_raises_value_error():
    with pytest.raises(ValueError, match="level cannot be empty"):
        build_learning_request(
            topic="Python",
            level="",
        )


def test_temperature_below_minimum_raises_value_error():
    with pytest.raises(ValueError):
        build_learning_request(
            topic="Python",
            level="beginner",
            temperature=-0.1,
        )


def test_invalid_max_tokens_raises_value_error():
    with pytest.raises(ValueError):
        build_learning_request(
            topic="Python",
            level="beginner",
            max_tokens=0,
        )


def test_max_tokens_above_limit_raises_value_error():
    with pytest.raises(ValueError):
        build_learning_request(
            topic="Python",
            level="beginner",
            max_tokens=5000,
        )


def test_whitespace_topic_is_rejected():
    with pytest.raises(ValueError):
        build_learning_request(
            topic="   ",
            level="beginner",
        )


def test_whitespace_level_is_rejected():
    with pytest.raises(ValueError):
        build_learning_request(
            topic="Python",
            level="   ",
        )