from data.question_bank import (
    QUESTION_BANK
)


def get_next_question(session):

    queue = session.investigation_queue

    for topic in queue:

        questions = QUESTION_BANK.get(
            topic,
            []
        )

        for question in questions:

            if (
                question
                not in session.asked_questions
            ):

                session.asked_questions.append(
                    question
                )

                return question

    for topic in session.active_topics:

        questions = QUESTION_BANK.get(
            topic,
            []
        )

        for question in questions:

            if (
                question
                not in session.asked_questions
            ):

                session.asked_questions.append(
                    question
                )

                return question

    general_questions = QUESTION_BANK[
        "general"
    ]

    for question in general_questions:

        if (
            question
            not in session.asked_questions
        ):

            session.asked_questions.append(
                question
            )

            return question

    return None