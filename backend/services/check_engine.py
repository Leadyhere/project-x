from data.check_questions import (
    CHECK_QUESTIONS
)

from services.investigation_engine import (
    get_missing_checks
)


def get_adaptive_check_question(

    session,

    topic
):

    missing_checks = (
        get_missing_checks(
            session,
            topic
        )
    )

    if not missing_checks:
        return None

    next_check = missing_checks[0]

    questions = CHECK_QUESTIONS.get(
        next_check,
        []
    )

    if not questions:
        return None

    return {
        "check": next_check,
        "question": questions[0]
    }