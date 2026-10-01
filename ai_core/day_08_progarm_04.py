def calculate_message_count(messages: list[dict[str, str]]) -> int:
    return len(messages)


def main() -> None:
    messages = [
        {"role": "system", "content": "You are helpful."},
        {"role": "user", "content": "Explain RAG."},
    ]

    print(f"Message count: {calculate_message_count(messages)}")


if __name__ == "__main__":
    main()