import numpy as np

document_embeddings = np.array([
    [0.2, 0.8, 0.1],
    [0.9, 0.1, 0.3],
    [0.5, 0.4, 0.7],
])

print("Matrix:")
print(document_embeddings)

print("\nShape:", document_embeddings.shape)
print("Column totals, axis=0:", document_embeddings.sum(axis=0))
print("Row totals, axis=1:", document_embeddings.sum(axis=1))