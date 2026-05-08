from data.investigation_graph import (
    INVESTIGATION_GRAPH
)


def get_missing_checks(

    session,

    topic
):

    graph = INVESTIGATION_GRAPH.get(
        topic,
        {}
    )

    required = graph.get(
        "required_checks",
        []
    )

    completed = (
        session.coverage_map.get(
            topic,
            []
        )
    )

    missing = [

        item

        for item in required

        if item not in completed
    ]

    return missing