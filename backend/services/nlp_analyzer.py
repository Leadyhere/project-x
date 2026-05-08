from data.topic_map import TOPIC_KEYWORDS


EMOTION_KEYWORDS = {

    "hopeless": [
        "hopeless",
        "worthless",
        "pointless"
    ],

    "anxious": [
        "panic",
        "anxious",
        "nervous"
    ],

    "lonely": [
        "alone",
        "isolated",
        "lonely"
    ],

    "overwhelmed": [
        "overwhelmed",
        "exhausted",
        "drained"
    ]
}


def analyze_message(message):

    message_lower = message.lower()

    detected_topics = []

    detected_emotions = []

    for topic, keywords in TOPIC_KEYWORDS.items():

        if any(k in message_lower for k in keywords):

            detected_topics.append(topic)

    for emotion, keywords in EMOTION_KEYWORDS.items():

        if any(k in message_lower for k in keywords):

            detected_emotions.append(emotion)

    return {
        "topics": detected_topics,
        "emotions": detected_emotions
    }