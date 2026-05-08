FUNCTIONAL_KEYWORDS = {

    "routine_disruption": [

        "can't get out of bed",

        "routine",

        "can't function",

        "everything feels hard"
    ],

    "sleep_disruption": [

        "can't sleep",

        "awake",

        "insomnia",

        "sleeping too much"
    ],

    "concentration_decline": [

        "can't focus",

        "can't concentrate",

        "mind wanders"
    ],

    "motivational_decline": [

        "no motivation",

        "don't feel like doing anything",

        "exhausted"
    ],

    "social_disconnection": [

        "alone",

        "isolated",

        "disconnected"
    ]
}


def update_functional_impairment(
    session,
    message
):

    message_lower = message.lower()

    profile = (
        session.psychological_profile
    )

    for category, keywords in (
        FUNCTIONAL_KEYWORDS.items()
    ):

        if any(

            keyword in message_lower

            for keyword in keywords
        ):

            profile[category] += 0.15

            profile[
                "functional_impairment"
            ] += 0.08

    profile[
        "functional_impairment"
    ] = min(
        profile["functional_impairment"],
        1.0
    )

    return profile