from ai_core.topic_tools import create_topic_slug, normalize_topic

topic = "  Retrieval   Augmented   Generation  "

print(normalize_topic(topic))
print(create_topic_slug(topic))