import json
from pathlib import Path

config_file = Path("data") / "ai_config.json"

config_file.parent.mkdir(parents=True, exist_ok=True)

config = {
    "model": "gpt-5",
    "temperature": 0.5,
    "max_tokens": 300,
    "tools_enabled": ["knowledge_search", "calculator"],
}

with config_file.open("w", encoding="utf-8") as file:
    json.dump(config, file, indent=2)

with config_file.open(encoding="utf-8") as file:
    loaded_config = json.load(file)

print("Loaded configuration:")
for key, value in loaded_config.items():
    print(f"{key}: {value}")