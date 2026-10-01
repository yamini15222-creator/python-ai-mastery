class InvalidTokenLimitError(ValueError):
    """Raised when a token limit is outside the allowed range."""


def validate_token_limit(max_tokens: int) -> int:
    if not 1 <= max_tokens <= 4_000:
        raise InvalidTokenLimitError(
            "max_tokens must be between 1 and 4000."
        )

    return max_tokens