import numpy as np

document_names = np.array([
    "rag_basics.txt",
    "python_functions.txt",
    "ai_agents.txt",
    "vector_databases.txt",
])

document_embeddings = np.array([
    [0.9, 0.1, 0.2],
    [0.1, 0.9, 0.1],
    [0.7, 0.2, 0.8],
    [0.8, 0.1, 0.7],
])

query_embedding = np.array([0.8, 0.1, 0.7])

scores = document_embeddings @ query_embedding
ranked_indexes = np.argsort(scores)[::-1]

print("Ranked search results:")

for index in ranked_indexes:
    print(f"{document_names[index]}: {scores[index]:.3f}")