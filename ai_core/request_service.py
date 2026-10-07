from .prompt_builder import build_ai_request


class RequestService:
    """Service responsible for preparing learner AI requests."""

    def create_request(self, topic: str, level: str) -> dict[str, str]:
        """Create a validated AI request."""
        return build_ai_request(topic, level)