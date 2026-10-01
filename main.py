from ai_core.config import ModelConfig
from ai_core.request_service import create_learning_request
from ai_core.request_summary import summarize_request


def main() -> None:
    config = ModelConfig(
        model="demo-llm",
        temperature=0.4,
        max_tokens=350,
    )

    request = create_learning_request(
        topic="Retrieval-Augmented Generation",
        level="beginner",
        config=config,
    )

    print(summarize_request(request))


if __name__ == "__main__":
    main()