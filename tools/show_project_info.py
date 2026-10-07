from ai_core.project_metadata import get_project_metadata

metadata = get_project_metadata()

print(f"Project: {metadata.name}")
print(f"Version: {metadata.version}")
print(f"Status: {metadata.status}")
print(f"Description: {metadata.description}")