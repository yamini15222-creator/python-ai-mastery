from dataclasses import dataclass


class InvalidAIRequestError(ValueError):
    """Raised when an AI request is invalid."""


@dataclass
class AIRequest:
    prompt: str
    model: str
    temperature: float
    max_tokens: int

    def __getitem__(self, key: str):
        data = {
            "prompt": self.prompt,
            "model": self.model,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "messages": [
                {
                    "role": "user",
                    "content": self.prompt,
                }
            ],
        }

        return data[key]


def create_ai_request(
    prompt: str,
    model: str = "gpt-5",
    temperature: float = 0.7,
    max_tokens: int = 500,
) -> AIRequest:

    prompt = prompt.strip()

    if not prompt:
        raise InvalidAIRequestError("Prompt cannot be empty.")

    if temperature < 0 or temperature > 2:
        raise InvalidAIRequestError(
            "Temperature must be between 0 and 2"
        )

    if max_tokens <= 0 or max_tokens > 4000:
        raise InvalidAIRequestError(
            "max_tokens must be between 1 and 4000"
        )

    return AIRequest(
        prompt=prompt,
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
    )