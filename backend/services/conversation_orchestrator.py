from models.session_model import SessionState

from services.nlp_analyzer import analyze_message

from services.memory_engine import update_memory

from services.psychological_state_engine import (
    update_psychological_state
)

from services.drift_engine import (
    detect_emotional_drift
)

from services.contradiction_engine import (
    detect_contradictions
)

from services.investigation_planner import (
    update_investigation_queue
)

from services.question_engine import (
    get_next_question
)

from services.risk_engine import (
    evaluate_risk
)

from services.confidence_engine import (
    calculate_confidence
)

from services.coverage_inference_engine import (
    infer_covered_checks
)

from services.reflection_engine import (
    generate_reflection
)

from services.semantic_risk_engine import (
    detect_semantic_risk
)

from services.narrative_depth_engine import (
    calculate_narrative_depth
)

from services.disclosure_detector import (
    should_trigger_probe
)

from services.check_engine import (
    get_adaptive_check_question
)

from services.coverage_tracker import (
    mark_coverage,
    initialize_coverage
)

from services.micro_probe_engine import (
    select_micro_probe
)

from services.functional_impairment_engine import (
    update_functional_impairment
)

from services.temporal_engine import (
    update_temporal_state
)

from services.conversation_ai_engine import (
    generate_response
)

sessions = {}


def start_session(user_id):

    session = SessionState(
        user_id=user_id
    )

    session.coverage_map = (
        initialize_coverage()
    )

    sessions[user_id] = session

    return {
        "response":
        "What made you decide to open this today?"
    }


def process_message(user_id, message):

    session = sessions.get(user_id)

    if not session:

        return {

            "error":
            "Session not found. Start session first."
        }

    analysis = analyze_message(message)

    inferred_checks = (
        infer_covered_checks(
            message
        )
    )

    for topic in session.investigation_queue:

        for check in inferred_checks:

            mark_coverage(

                session,

                topic,

                check
            )

    update_functional_impairment(
        session,
        message
    )

    update_temporal_state(
        session,
        message
    )

    narrative_depth = (
        calculate_narrative_depth(
            message
        )
    )

    session.narrative_depth_score = (
        narrative_depth
    )

    probe_trigger = (
        should_trigger_probe(

            session,

            narrative_depth,

            analysis
        )
    )

    micro_probe = None

    if probe_trigger:

        micro_probe = (
            select_micro_probe(
                session
            )
        )

    semantic_risk = detect_semantic_risk(
        message
    )

    if semantic_risk:

        analysis["topics"].append(
            "suicidal"
        )

    update_memory(
        session,
        message,
        analysis
    )

    psychological_profile = (
        update_psychological_state(
            session,
            analysis
        )
    )

    session.emotional_states.append(
        psychological_profile.copy()
    )

    drift = detect_emotional_drift(
        session
    )

    contradiction = detect_contradictions(
        session,
        message
    )

    update_investigation_queue(
        session
    )

    risk = evaluate_risk(session)

    confidence = calculate_confidence(
        session
    )

    session.escalation_level = risk

    session.confidence_score = confidence

    reflection = generate_reflection(
        session,
        analysis
    )

    next_question = None

    for topic in session.investigation_queue:

        adaptive_check = (
            get_adaptive_check_question(
                session,
                topic
            )
        )

        if adaptive_check:

            next_question = (
                adaptive_check["question"]
            )

            mark_coverage(

                session,

                topic,

                adaptive_check["check"]
            )

            break

    if not next_question:

        next_question = get_next_question(
            session
        )

    if micro_probe:

        next_question = micro_probe

    if not next_question:

        return {

            "completed": True,

            "risk": risk,

            "confidence": confidence,

            "reflection": reflection
        }

    ai_response = generate_response(

        user_message=message,

        reflection=reflection,

        next_question=next_question,

        conversation_history=(
            session.conversation_history
        )
    )

    return {

        "completed": False,

        "response": ai_response,

        "risk": risk,

        "confidence": confidence,

        "drift_detected": drift,

        "contradiction_detected":
        contradiction,

        "investigation_queue":
        session.investigation_queue
    }