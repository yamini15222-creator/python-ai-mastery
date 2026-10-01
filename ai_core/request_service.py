from typing import Any

from ai_core.config import ModelConfig
from ai_core.prompt_builder import build_tutor_instruction


def create_learning_request(
    topic: str,
    level: str,
    config: ModelConfig,
) -> dict[str, Any]:
    """Create a learning request using a ModelConfig."""

    instruction = build_tutor_instruction(topic, level)

    return {
        "model": config.model,
        "temperature": config.temperature,
        "max_tokens": config.max_tokens,
        "messages": [
            {
                "role": "system",
                "content": instruction,
            },
            {
                "role": "user",
                "content": f"Teach me about {topic.strip()}.",
            },
        ],
    }


def build_learning_request(
    topic: str,
    level: str,
    model: str = "gpt-4o-mini",
    temperature: float = 0.7,
    max_tokens: int = 500,
) -> dict[str, Any]:
    """Build a learning request with direct model configuration."""

    if not isinstance(topic, str) or not topic.strip():
        raise ValueError("topic cannot be empty")

    if not isinstance(level, str) or not level.strip():
        raise ValueError("level cannot be empty")

    if not isinstance(temperature, (int, float)) or not 0 <= temperature <= 2:
        raise ValueError("temperature must be between 0 and 2")

    if not isinstance(max_tokens, int) or not 1 <= max_tokens <= 4096:
        raise ValueError("max_tokens must be between 1 and 4096")

    config = ModelConfig(
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    return create_learning_request(
        topic=topic,
        level=level,
        config=config,
    )