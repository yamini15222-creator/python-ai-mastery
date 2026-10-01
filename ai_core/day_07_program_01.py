from pathlib import Path

prompt_file = Path("data") / "prompts" / "rag_prompt.txt"

prompt_file.parent.mkdir(parents=True, exist_ok=True)

prompt = "Explain RAG with one practical Python example."

prompt_file.write_text(prompt, encoding="utf-8")

saved_prompt = prompt_file.read_text(encoding="utf-8")

print(f"Saved prompt: {saved_prompt}")
print(f"File location: {prompt_file}")