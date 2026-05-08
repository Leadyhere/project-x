def update_memory(session, user_message, analysis):

    session.conversation_history.append({
        "role": "user",
        "message": user_message
    })

    for topic in analysis["topics"]:

        if topic not in session.active_topics:
            session.active_topics.append(topic)

    return session