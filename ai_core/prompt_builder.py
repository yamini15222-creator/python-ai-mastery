def build_tutor_instruction(topic: str, level: str) -> str:
    cleaned_topic = topic.strip()
    cleaned_level = level.strip()

    if not cleaned_topic:
        raise ValueError("Topic cannot be empty.")

    if not cleaned_level:
        raise ValueError("Level cannot be empty.")

    return (
        "You are a helpful Python and AI tutor. "
        f"Explain {cleaned_topic} for a {cleaned_level} learner. "
        "Use plain language and one practical example."
    )