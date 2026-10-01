prompt = "Explain Python"
print("Before:", prompt, id(prompt))

prompt += " with examples"
print("After: ", prompt, id(prompt))

history = ["Hello"]
print("\nBefore:", history, id(history))

history.append("Explain Python with examples")
print("After: ", history, id(history))