def calculate_confidence(
    session
):

    confidence = 0.3

    confidence += min(

        session.narrative_depth_score,

        0.3
    )

    confidence += min(

        len(
            session.conversation_history
        ) * 0.03,

        0.3
    )

    if session.coverage_map:

        completed = 0

        total = 0

        for topic in (
            session.coverage_map
        ):

            for check in (
                session.coverage_map[
                    topic
                ]
            ):

                total += 1

                if (
                    session.coverage_map[
                        topic
                    ][check]
                ):

                    completed += 1

        if total > 0:

            confidence += (
                completed / total
            ) * 0.4

    return round(
        min(confidence, 1.0),
        2
    )