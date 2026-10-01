from pathlib import Path


REQUIRED_PATHS = [
    Path("README.md"),
    Path(".gitignore"),
    Path("main.py"),
    Path("ai_core"),
    Path("tests"),
]


def audit_project(root: Path) -> bool:
    all_present = True

    for required_path in REQUIRED_PATHS:
        full_path = root / required_path
        exists = full_path.exists()

        status = "FOUND" if exists else "MISSING"
        print(f"{status}: {required_path}")

        if not exists:
            all_present = False

    return all_present


if __name__ == "__main__":
    project_root = Path(".")

    if audit_project(project_root):
        print("\nProject structure is ready.")
    else:
        print("\nProject structure needs attention.")