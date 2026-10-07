import numpy as np


def cosine_similarity(
    query_vector: np.ndarray,
    document_vector: np.ndarray,
) -> float:
    """Calculate cosine similarity between two vectors."""
    query_norm = np.linalg.norm(query_vector)
    document_norm = np.linalg.norm(document_vector)

    if query_norm == 0 or document_norm == 0:
        return 0.0

    return float(
        np.dot(query_vector, document_vector)
        / (query_norm * document_norm)
    )


def rank_documents(
    query_vector: np.ndarray,
    document_vectors: np.ndarray,
    document_names: list[str],
) -> list[tuple[str, float]]:
    """Rank documents by cosine similarity."""
    if len(document_vectors) != len(document_names):
        raise ValueError(
            "Document vectors and names must have the same length."
        )

    results = []

    for name, vector in zip(document_names, document_vectors):
        score = cosine_similarity(query_vector, vector)
        results.append((name, score))

    return sorted(
        results,
        key=lambda item: item[1],
        reverse=True,
    )


def find_most_relevant(
    query_vector: np.ndarray,
    document_vectors: np.ndarray,
    document_names: list[str],
) -> str:
    """Return the name of the most relevant document."""
    ranked = rank_documents(
        query_vector,
        document_vectors,
        document_names,
    )

    if not ranked:
        raise ValueError("No documents available.")

    return ranked[0][0]