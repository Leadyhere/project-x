def evaluate_risk(session):

    profile = (
        session.psychological_profile
    )

    risk_score = 0

    risk_score += profile.get(
        "distress_level",
        0
    )

    risk_score += profile.get(
        "future_orientation_decline",
        0
    )

    risk_score += profile.get(
        "self_harm_risk",
        0
    ) * 2

    if risk_score >= 2.2:

        return "high"

    if risk_score >= 1.2:

        return "moderate"

    return "low"