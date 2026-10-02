import numpy as np
import pytest

from ai_core.vector_search import find_similar_documents


def test_returns_documents_in_descending_score_order():
    documents = ["doc1.txt", "doc2.txt", "doc3.txt"]

    embeddings = np.array([
        [1.0, 0.0],
        [0.5, 0.5],
        [0.0, 1.0],
    ])

    query = np.array([1.0, 0.0])

    results = find_similar_documents(
        documents,
        embeddings,
        query,
        top_k=2,
    )

    assert results == [
        {"document": "doc1.txt", "score": 1.0},
        {"document": "doc2.txt", "score": 0.5},
    ]


def test_rejects_empty_document_list():
    embeddings = np.array([[1.0, 0.0]])
    query = np.array([1.0, 0.0])

    with pytest.raises(ValueError, match="document_names"):
        find_similar_documents([], embeddings, query, top_k=1)


def test_rejects_mismatched_dimensions():
    documents = ["doc1.txt"]

    embeddings = np.array([[1.0, 0.0]])
    query = np.array([1.0, 0.0, 0.0])

    with pytest.raises(ValueError, match="dimensions"):
        find_similar_documents(documents, embeddings, query, top_k=1)


def test_rejects_invalid_top_k():
    documents = ["doc1.txt"]
    embeddings = np.array([[1.0, 0.0]])
    query = np.array([1.0, 0.0])

    with pytest.raises(ValueError, match="top_k"):
        find_similar_documents(documents, embeddings, query, top_k=0)