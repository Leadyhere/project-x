def generate_reflection(session, analysis):

    emotions = analysis["emotions"]

    if "overwhelmed" in emotions:
        return (
            "It sounds like things have been "
            "feeling mentally exhausting lately."
        )

    if "hopeless" in emotions:
        return (
            "It seems like things may have been "
            "feeling emotionally heavy for a while."
        )

    if "lonely" in emotions:
        return (
            "It sounds like you’ve been feeling "
            "emotionally disconnected from others."
        )

    return (
        "I appreciate you sharing that."
    )