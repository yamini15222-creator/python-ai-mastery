original_history = ["Hello", "What is an LLM?"]

shared_history = original_history
shared_history.append("What is RAG?")

print("Original after shared reference:")
print(original_history)

safe_history = original_history.copy()
safe_history.append("What is a vector database?")

print("\nOriginal after copy:")
print(original_history)

print("\nCopied history:")
print(safe_history)