raw_prompts = [
    " Explain Python lists ",
    "",
    "   ",
    "What is RAG?",
    " Explain AI agents ",
]

clean_prompts = [
    prompt.strip()
    for prompt in raw_prompts
    if prompt.strip()
]

for index, prompt in enumerate(clean_prompts, start=1):
    print(f"{index}. {prompt}")