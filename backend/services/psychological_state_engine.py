TOPIC_TO_PROFILE_MAP = {

    "sadness": "distress_level",

    "anxiety": "cognitive_overactivation",

    "future_loss":
    "future_orientation_decline",

    "withdrawal":
    "social_disconnection",

    "exhaustion":
    "motivational_decline",

    "suicidal":
    "self_harm_risk"
}


def update_psychological_state(

    session,

    analysis
):

    profile = (
        session.psychological_profile
    )

    topics = analysis.get(
        "topics",
        []
    )

    emotions = analysis.get(
        "emotions",
        []
    )

    for topic in topics:

        mapped_state = (
            TOPIC_TO_PROFILE_MAP.get(
                topic
            )
        )

        if mapped_state:

            if mapped_state not in profile:

                profile[
                    mapped_state
                ] = 0.0

            profile[
                mapped_state
            ] += 0.15

    for emotion in emotions:

        emotion_lower = emotion.lower()

        if emotion_lower in [

            "overwhelmed",

            "drained",

            "empty"
        ]:

            profile[
                "distress_level"
            ] += 0.10

    for key in profile:

        profile[key] = min(
            profile[key],
            1.0
        )

    return profile