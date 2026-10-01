from dataclasses import dataclass


@dataclass(frozen=True)
class ModelConfig:
    model: str = "demo-llm"
    temperature: float = 0.5
    max_tokens: int = 500

    def __post_init__(self) -> None:
        if not self.model.strip():
            raise ValueError("Model name cannot be empty.")

        if not 0 <= self.temperature <= 2:
            raise ValueError("Temperature must be between 0 and 2.")

        if not 1 <= self.max_tokens <= 4_000:
            raise ValueError("max_tokens must be between 1 and 4000.")