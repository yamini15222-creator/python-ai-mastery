from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
CONVERSATION_FILE = DATA_DIR / "conversations.json"
DOCUMENT_FILE = DATA_DIR / "documents.json"

MIN_TOPIC_LENGTH = 2
MAX_TOPIC_LENGTH = 100

SUPPORTED_LEVELS = {
    "beginner",
    "intermediate",
    "advanced",
}