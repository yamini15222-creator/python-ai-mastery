from .config import MAX_TOPIC_LENGTH, MIN_TOPIC_LENGTH, SUPPORTED_LEVELS


def validate_topic(topic: str) -> str:
    """Validate and normalize a learner topic."""
    if not isinstance(topic, str):
        raise TypeError("Topic must be a string.")

    cleaned_topic = topic.strip()

    if len(cleaned_topic) < MIN_TOPIC_LENGTH:
        raise ValueError(
            f"Topic must contain at least {MIN_TOPIC_LENGTH} characters."
        )

    if len(cleaned_topic) > MAX_TOPIC_LENGTH:
        raise ValueError(
            f"Topic must not exceed {MAX_TOPIC_LENGTH} characters."
        )

    return cleaned_topic


def validate_level(level: str) -> str:
    """Validate and normalize the learner level."""
    if not isinstance(level, str):
        raise TypeError("Level must be a string.")

    cleaned_level = level.strip().lower()

    if cleaned_level not in SUPPORTED_LEVELS:
        valid_levels = ", ".join(sorted(SUPPORTED_LEVELS))
        raise ValueError(
            f"Invalid level. Choose one of: {valid_levels}."
        )

    return cleaned_level


def build_ai_request(topic: str, level: str) -> dict[str, str]:
    """Build a validated AI request for future LLM integration."""
    validated_topic = validate_topic(topic)
    validated_level = validate_level(level)

    prompt = (
        f"Teach me about {validated_topic}. "
        f"My learning level is {validated_level}. "
        "Explain the concept clearly with examples and practical guidance."
    )

    return {
        "topic": validated_topic,
        "level": validated_level,
        "prompt": prompt,
    }