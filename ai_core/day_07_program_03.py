import json
from pathlib import Path


def load_json_file(file_path: Path) -> dict[str, object] | None:
    try:
        with file_path.open(encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Invalid JSON: {file_path}")
        return None


missing_file = Path("data") / "does_not_exist.json"

data = load_json_file(missing_file)

if data is None:
    print("No configuration was loaded.")
else:
    print(data)