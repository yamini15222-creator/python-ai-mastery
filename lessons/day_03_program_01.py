def create_model_config(
    model: str,
    *,
    temperature: float = 0.7,
    max_tokens: int = 500,
) -> dict[str, object]:
    if not 0 <= temperature <= 2:
        raise ValueError("Temperature must be between 0 and 2.")

    if max_tokens <= 0:
        raise ValueError("max_tokens must be greater than 0.")

    return {
        "model": model,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }


config = create_model_config(
    "gpt-5",
    temperature=0.3,
    max_tokens=250,
)

print(config)