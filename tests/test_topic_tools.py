import pytest

from ai_core.topic_tools import create_topic_slug, normalize_topic


def test_normalize_topic_removes_extra_whitespace() -> None:
    assert normalize_topic("  AI   agents  ") == "AI agents"


def test_create_topic_slug() -> None:
    assert create_topic_slug("Vector Database") == "vector-database"


def test_normalize_topic_rejects_empty_value() -> None:
    with pytest.raises(ValueError, match="Topic cannot be empty"):
        normalize_topic("   ")