import numpy as np

from ai_core.agent_state import AgentState
from ai_core.config import CONVERSATION_FILE
from ai_core.conversation_store import ConversationStore
from ai_core.request_service import RequestService
from ai_core.vector_search import find_most_relevant


def main() -> None:
    """Run the AI Learning Assistant prototype."""

    print("=== AI Learning Assistant ===")

    topic = input("Enter learning topic: ")
    level = input(
        "Enter level (beginner/intermediate/advanced): "
    )

    request_service = RequestService()

    try:
        request = request_service.create_request(topic, level)
    except (TypeError, ValueError) as error:
        print(f"Input error: {error}")
        return

    state = AgentState(
        topic=request["topic"],
        level=request["level"],
    )

    state.add_message(
        "user",
        request["prompt"],
    )

    store = ConversationStore(CONVERSATION_FILE)
    store.save(state.history)

    vocabulary = [
        "python",
        "numpy",
        "machine",
        "learning",
        "nlp",
    ]

    documents = {
        "Python Basics": [1, 0, 0, 0, 0],
        "NumPy Fundamentals": [0, 1, 0, 0, 0],
        "Machine Learning Introduction": [0, 0, 1, 1, 0],
        "Natural Language Processing": [0, 0, 0, 0, 1],
    }

    query = request["topic"].lower()

    query_vector = np.array(
        [
            int(word in query)
            for word in vocabulary
        ],
        dtype=float,
    )

    document_names = list(documents.keys())
    document_vectors = np.array(
        list(documents.values()),
        dtype=float,
    )

    most_relevant = find_most_relevant(
        query_vector,
        document_vectors,
        document_names,
    )

    print("\nValidated Request:")
    print(request)

    print("\nMost Relevant Learning Material:")
    print(most_relevant)

    print("\nConversation history saved successfully.")


if __name__ == "__main__":
    main()