def detect_emotional_drift(
    session
):

    states = (
        session.emotional_states
    )

    if len(states) < 2:

        return False

    previous = states[-2]

    current = states[-1]

    important_states = [

        "distress_level",

        "future_orientation_decline",

        "social_disconnection",

        "motivational_decline"
    ]

    for state in important_states:

        previous_value = previous.get(
            state,
            0
        )

        current_value = current.get(
            state,
            0
        )

        if (

            current_value -
            previous_value

        ) > 0.3:

            return True

    return False