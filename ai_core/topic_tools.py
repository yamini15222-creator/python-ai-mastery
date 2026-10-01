def normalize_topic(topic: str) -> str:
    cleaned_topic = " ".join(topic.split())

    if not cleaned_topic:
        raise ValueError("Topic cannot be empty.")

    return cleaned_topic


def create_topic_slug(topic: str) -> str:
    normalized_topic = normalize_topic(topic)

    return normalized_topic.lower().replace(" ", "-")