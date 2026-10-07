import numpy as np

query_embedding = np.array([0.8, 0.1, 0.7])
document_embedding = np.array([0.7, 0.2, 0.8])

print("Element-wise multiplication:")
print(query_embedding * document_embedding)

print("\nDot-product similarity score:")
print(query_embedding @ document_embedding)