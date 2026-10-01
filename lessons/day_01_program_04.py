ai_request = {
    "model": "gpt-5",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful Python tutor.",
        },
        {
            "role": "user",
            "content": "Explain Python dictionaries.",
        },
    ],
    "temperature": 0.5,
    "max_tokens": 300,
}

print("Model:", ai_request["model"])
print("User question:", ai_request["messages"][1]["content"])
print("Temperature:", ai_request["temperature"])