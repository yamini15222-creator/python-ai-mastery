import numpy as np

from ai_core.vector_search import (
    cosine_similarity,
    find_most_relevant,
    rank_documents,
)


def test_cosine_similarity() -> None:
    vector_a = np.array([1.0, 0.0])
    vector_b = np.array([1.0, 0.0])

    assert cosine_similarity(vector_a, vector_b) == 1.0


def test_documents_are_ranked() -> None:
    query = np.array([1.0, 0.0])

    documents = np.array(
        [
            [1.0, 0.0],
            [0.0, 1.0],
            [0.5, 0.5],
        ]
    )

    names = [
        "Document A",
        "Document B",
        "Document C",
    ]

    results = rank_documents(
        query,
        documents,
        names,
    )

    assert results[0][0] == "Document A"


def test_most_relevant_document() -> None:
    query = np.array([0.0, 1.0])

    documents = np.array(
        [
            [1.0, 0.0],
            [0.0, 1.0],
            [0.5, 0.5],
        ]
    )

    names = [
        "Python",
        "NumPy",
        "Machine Learning",
    ]

    result = find_most_relevant(
        query,
        documents,
        names,
    )

    assert result == "NumPy"