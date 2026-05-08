def update_investigation_queue(
    session
):

    profile = (
        session.psychological_profile
    )

    queue = []

    if profile.get(

        "distress_level",
        0

    ) > 0.4:

        queue.append(
            "distress"
        )

    if profile.get(

        "cognitive_overactivation",
        0

    ) > 0.4:

        queue.append(
            "overthinking"
        )

    if profile.get(

        "future_orientation_decline",
        0

    ) > 0.4:

        queue.append(
            "future_outlook"
        )

    if profile.get(

        "social_disconnection",
        0

    ) > 0.4:

        queue.append(
            "relationships"
        )

    if profile.get(

        "motivational_decline",
        0

    ) > 0.4:

        queue.append(
            "daily_functioning"
        )

    if profile.get(

        "self_harm_risk",
        0

    ) > 0.5:

        queue.insert(
            0,
            "safety"
        )

    session.investigation_queue = (
        queue
    )