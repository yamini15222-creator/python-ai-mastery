def get_user_prompt(request: dict[str, str]) -> str:
    try:
        prompt = request["prompt"].strip()
    except KeyError as error:
        raise ValueError("Request must include a 'prompt' field.") from error

    if not prompt:
        raise ValueError("Prompt cannot be empty.")

    return prompt


requests = [
    {"prompt": "Explain RAG."},
    {},
    {"prompt": "   "},
]

for request in requests:
    try:
        print(get_user_prompt(request))
    except ValueError as error:
        print(f"Invalid request: {error}")