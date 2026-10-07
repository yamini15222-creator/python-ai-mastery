import numpy as np

document_names = np.array([
    "rag_basics.txt",
    "python_lists.txt",
    "ai_agents.txt",
])

# Demo vectors only. Real embedding models generate these values.
document_embeddings = np.array([
    [0.9, 0.1, 0.2],
    [0.1, 0.9, 0.1],
    [0.7, 0.2, 0.8],
])

query_embedding = np.array([0.8, 0.1, 0.7])

similarity_scores = document_embeddings @ query_embedding

best_index = int(np.argmax(similarity_scores))
best_document = document_names[best_index]
best_score = similarity_scores[best_index]

print("Document matrix shape:", document_embeddings.shape)
print("\nSimilarity scores:")

for name, score in zip(document_names, similarity_scores, strict=True):
    print(f"{name}: {score:.3f}")

print(f"\nBest matching document: {best_document}")
print(f"Score: {best_score:.3f}")