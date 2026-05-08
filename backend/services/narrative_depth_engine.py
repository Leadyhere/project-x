def calculate_narrative_depth(message):

    word_count = len(
        message.split()
    )

    emotional_keywords = [

        "feel",

        "because",

        "alone",

        "tired",

        "stuck",

        "hard",

        "overwhelmed"
    ]

    emotional_score = sum(

        1

        for word
        in emotional_keywords

        if word in message.lower()
    )

    depth_score = (
        word_count * 0.02
        +
        emotional_score * 0.1
    )

    return min(depth_score, 1.0)