model_name = "gpt-5"
temperature = 0.7
max_tokens = 500
is_available = True

for value in [model_name, temperature, max_tokens, is_available]:
    print(f"Value: {value}")
    print(f"Type: {type(value).__name__}")
    print(f"Object ID: {id(value)}")
    print("-" * 30)