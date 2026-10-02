import numpy as np


def find_similar_documents(
    document_names: list[str],
    document_embeddings: np.ndarray,
    query_embedding: np.ndarray,
    top_k: int,
) -> list[dict[str, float | str]]:
    """Return the documents with the highest dot-product similarity."""

    if not document_names:
        raise ValueError("document_names cannot be empty")

    if top_k < 1:
        raise ValueError("top_k must be at least 1")

    document_embeddings = np.asarray(document_embeddings, dtype=float)
    query_embedding = np.asarray(query_embedding, dtype=float)

    if document_embeddings.ndim != 2:
        raise ValueError("document_embeddings must be a 2D matrix")

    if query_embedding.ndim != 1:
        raise ValueError("query_embedding must be a 1D vector")

    if len(document_names) != document_embeddings.shape[0]:
        raise ValueError(
            "Number of document names must match number of embeddings"
        )

    if document_embeddings.shape[1] != query_embedding.shape[0]:
        raise ValueError("Embedding dimensions do not match")

    scores = document_embeddings @ query_embedding

    top_k = min(top_k, len(document_names))

    top_indices = np.argsort(scores)[::-1][:top_k]

    return [
        {
            "document": document_names[index],
            "score": round(float(scores[index]), 2),
        }
        for index in top_indices
    ]