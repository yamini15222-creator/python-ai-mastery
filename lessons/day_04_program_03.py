import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


def process_prompt(prompt: str) -> str:
    cleaned_prompt = prompt.strip()

    if not cleaned_prompt:
        logger.warning("Received an empty prompt.")
        raise ValueError("Prompt cannot be empty.")

    logger.info("Processing prompt with %s characters.", len(cleaned_prompt))

    return f"AI response placeholder for: {cleaned_prompt}"


for prompt in ["What is an AI agent?", "   ", "Explain embeddings."]:
    try:
        print(process_prompt(prompt))
    except ValueError as error:
        logger.error("Prompt processing failed: %s", error)