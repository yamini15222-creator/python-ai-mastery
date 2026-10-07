import pytest

from ai_core.request_service import RequestService


def test_create_valid_request() -> None:
    """Test that a valid AI request is created."""
    service = RequestService()

    result = service.create_request(
        "Python",
        "beginner",
    )

    assert result["topic"] == "Python"
    assert result["level"] == "beginner"
    assert "Python" in result["prompt"]
    assert "beginner" in result["prompt"]


def test_create_request_strips_topic_whitespace() -> None:
    """Test that whitespace around the topic is removed."""
    service = RequestService()

    result = service.create_request(
        "  NumPy  ",
        "beginner",
    )

    assert result["topic"] == "NumPy"


def test_create_request_normalizes_level() -> None:
    """Test that the learner level is converted to lowercase."""
    service = RequestService()

    result = service.create_request(
        "Machine Learning",
        "BEGINNER",
    )

    assert result["level"] == "beginner"


def test_invalid_topic_raises_value_error() -> None:
    """Test that an invalid topic raises ValueError."""
    service = RequestService()

    with pytest.raises(ValueError):
        service.create_request(
            "",
            "beginner",
        )


def test_invalid_level_raises_value_error() -> None:
    """Test that an invalid level raises ValueError."""
    service = RequestService()

    with pytest.raises(ValueError):
        service.create_request(
            "Python",
            "expert",
        )


def test_invalid_topic_type_raises_type_error() -> None:
    """Test that a non-string topic raises TypeError."""
    service = RequestService()

    with pytest.raises(TypeError):
        service.create_request(
            123,  # type: ignore[arg-type]
            "beginner",
        )


def test_invalid_level_type_raises_type_error() -> None:
    """Test that a non-string level raises TypeError."""
    service = RequestService()

    with pytest.raises(TypeError):
        service.create_request(
            "Python",
            123,  # type: ignore[arg-type]
        )