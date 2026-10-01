def validate_max_tokens(max_tokens: int) -> int:
    if max_tokens <= 0:
        raise ValueError("max_tokens must be greater than zero.")

    return max_tokens


values = [500, 0, -10]

for value in values:
    try:
        result = validate_max_tokens(value)
        print(f"{result} is valid.")
    except ValueError as error:
        print(f"{value} is invalid: {error}")