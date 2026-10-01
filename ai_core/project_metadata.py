from dataclasses import dataclass


@dataclass(frozen=True)
class ProjectMetadata:
    name: str
    version: str
    description: str
    status: str


def get_project_metadata() -> ProjectMetadata:
    return ProjectMetadata(
        name="Python AI Mastery",
        version="0.1.0",
        description="Modular AI learning-request builder.",
        status="Development",
    )