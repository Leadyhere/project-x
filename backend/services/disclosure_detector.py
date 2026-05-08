def should_trigger_probe(

    session,

    narrative_depth,

    analysis

):

    short_response = (
        narrative_depth < 0.25
    )

    unresolved_topics = (
        len(session.investigation_queue)
        > 0
    )

    emotional_signal_present = (
        len(analysis["emotions"])
        > 0
    )

    if (
        short_response
        and emotional_signal_present
    ):
        return True

    if (
        short_response
        and unresolved_topics
    ):
        return True

    return False