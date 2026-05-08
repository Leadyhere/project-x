def track_probe_effectiveness(

    session,

    probe,

    response,

    depth_score,

    new_topics

):

    effectiveness = {

        "probe": probe,

        "response_length":
        len(response.split()),

        "depth_score":
        depth_score,

        "new_topics":
        len(new_topics)
    }

    session.probe_memory.append(
        effectiveness
    )