def initialize_coverage():

    return {

        "sleep": [],

        "social_disconnection": [],

        "functional_impairment": [],

        "future_orientation": [],

        "risk_sensing": []
    }


def mark_coverage(

    session,

    topic,

    check
):

    if (
        topic
        not in session.coverage_map
    ):

        session.coverage_map[topic] = []

    if (
        check
        not in session.coverage_map[topic]
    ):

        session.coverage_map[
            topic
        ].append(check)