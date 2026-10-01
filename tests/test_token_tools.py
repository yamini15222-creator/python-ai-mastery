import pytest

from ai_core.token_tools import InvalidTokenLimitError, validate_token_limit


def test_validate_token_limit_accepts_valid_value() -> None:
    assert validate_token_limit(500) == 500


@pytest.mark.parametrize("max_tokens", [0, -1, 4_001])
def test_validate_token_limit_rejects_invalid_values(
    max_tokens: int,
) -> None:
    with pytest.raises(InvalidTokenLimitError, match="max_tokens"):
        validate_token_limit(max_tokens)