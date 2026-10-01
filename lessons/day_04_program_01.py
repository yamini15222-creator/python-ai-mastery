def parse_max_tokens(raw_value: str) -> int:
    try:
        max_tokens = int(raw_value)
    except ValueError as error:
        raise ValueError(
            f"max_tokens must be a whole number; received {raw_value!r}."
        ) from error

    if not 1 <= max_tokens <= 4_000:
        raise ValueError("max_tokens must be between 1 and 4000.")

    return max_tokens


for raw_value in ["500", "0", "5000", "abc"]:
    try:
        print(f"{raw_value!r} -> {parse_max_tokens(raw_value)}")
    except ValueError as error:
        print(f"{raw_value!r} -> Error: {error}")