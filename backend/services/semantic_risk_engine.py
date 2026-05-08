SEMANTIC_RISK_PHRASES = [

    "what's the point",

    "tired of everything",

    "can't do this anymore",

    "people would be better without me",

    "i want everything to stop"
]


def detect_semantic_risk(message):

    message_lower = message.lower()

    for phrase in SEMANTIC_RISK_PHRASES:

        if phrase in message_lower:

            return True

    return False