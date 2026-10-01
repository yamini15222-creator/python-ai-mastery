import pytest

from ai_core.request_tools import InvalidAIRequestError, create_ai_request


def test_create_ai_request_uses_default_values() -> None:
    request = create_ai_request("What is a vector database?")

    assert request.model == "gpt-5"
    assert request.temperature == 0.7
    assert request.max_tokens == 500




def test_create_ai_request_returns_expected_data() -> None:
    request = create_ai_request(
        " Explain RAG simply. ",
        model="gpt-5",
        temperature=0.5,
        max_tokens=300,
    )

    assert request["model"] == "gpt-5"
    assert request["temperature"] == 0.5
    assert request["max_tokens"] == 300
    assert request["messages"][0]["role"] == "user"
    assert request["messages"][0]["content"] == "Explain RAG simply."


def test_create_ai_request_rejects_empty_prompt() -> None:
    with pytest.raises(InvalidAIRequestError, match="Prompt cannot be empty"):
        create_ai_request("   ")


@pytest.mark.parametrize("temperature", [-0.1, 2.1, 5])
def test_create_ai_request_rejects_invalid_temperature(
    temperature: float,
) -> None:
    with pytest.raises(InvalidAIRequestError, match="Temperature"):
        create_ai_request("Explain embeddings.", temperature=temperature)


@pytest.mark.parametrize("max_tokens", [0, -1, 4_001])
def test_create_ai_request_rejects_invalid_max_tokens(
    max_tokens: int,
) -> None:
    with pytest.raises(InvalidAIRequestError, match="max_tokens"):
        create_ai_request("Explain AI agents.", max_tokens=max_tokens)

def test_create_ai_request_trims_prompt_whitespace() -> None:
    request = create_ai_request("   Explain AI agents.   ")

    assert request["messages"][0]["content"] == "Explain AI agents."