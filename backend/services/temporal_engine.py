TEMPORAL_KEYWORDS = {

    "persistent": [

        "for months",

        "for a long time",

        "always",

        "constantly"
    ],

    "worsening": [

        "getting worse",

        "worse lately",

        "more intense",

        "spiraling"
    ],

    "recent": [

        "recently",

        "past few days",

        "lately"
    ]
}


def update_temporal_state(
    session,
    message
):

    message_lower = message.lower()

    profile = (
        session.psychological_profile
    )

    for keyword in (
        TEMPORAL_KEYWORDS["persistent"]
    ):

        if keyword in message_lower:

            profile[
                "persistence_score"
            ] += 0.20

    for keyword in (
        TEMPORAL_KEYWORDS["worsening"]
    ):

        if keyword in message_lower:

            profile[
                "escalation_score"
            ] += 0.25

    profile[
        "persistence_score"
    ] = min(
        profile["persistence_score"],
        1.0
    )

    profile[
        "escalation_score"
    ] = min(
        profile["escalation_score"],
        1.0
    )

    return profile