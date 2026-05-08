CONTRADICTION_PAIRS = [

    ("supported", "alone"),

    ("okay", "hopeless"),

    ("fine", "worthless")
]


def detect_contradictions(session, message):

    message_lower = message.lower()

    for positive, negative in CONTRADICTION_PAIRS:

        previous_positive = any(
            positive in item["message"].lower()
            for item in session.conversation_history
        )

        current_negative = negative in message_lower

        if previous_positive and current_negative:

            contradiction = {
                "positive": positive,
                "negative": negative
            }

            session.contradictions.append(
                contradiction
            )

            return contradiction

    return None