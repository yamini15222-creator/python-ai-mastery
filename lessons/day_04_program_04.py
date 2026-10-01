class InvalidAIRequestError(ValueError):
    """Raised when an AI request does not meet application rules."""


def validate_model(model: str) -> str:
    allowed_models = {"gpt-5", "gpt-4.1", "local-model"}

    if model not in allowed_models:
        raise InvalidAIRequestError(
            f"Unsupported model: {model}. Choose one of {sorted(allowed_models)}."
        )

    return model


for model in ["gpt-5", "unknown-model"]:
    try:
        print(f"Using model: {validate_model(model)}")
    except InvalidAIRequestError as error:
        print(f"Request rejected: {error}")