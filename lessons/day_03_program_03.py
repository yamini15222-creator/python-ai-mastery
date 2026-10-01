def build_learning_prompt(
    topic: str,
    *,
    level: str = "beginner",
    include_example: bool = True,
) -> str:
    cleaned_topic = topic.strip()

    if not cleaned_topic:
        raise ValueError("Topic cannot be empty.")

    prompt = f"Explain {cleaned_topic} for a {level} learner."

    if include_example:
        prompt += " Include one practical Python example."

    return prompt


print(build_learning_prompt(" Python dictionaries "))
print(build_learning_prompt("Embeddings", level="advanced", include_example=False))