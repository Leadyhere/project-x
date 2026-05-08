from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class SessionState:

    user_id: str

    conversation_history: List[Dict] = field(default_factory=list)

    active_topics: List[str] = field(default_factory=list)

    completed_topics: List[str] = field(default_factory=list)

    asked_questions: List[str] = field(default_factory=list)

    emotional_states: List[Dict] = field(default_factory=list)

    contradictions: List[Dict] = field(default_factory=list)

    emotional_drifts: List[Dict] = field(default_factory=list)

    risk_flags: List[str] = field(default_factory=list)

    investigation_queue: List[str] = field(default_factory=list)
    coverage_map: Dict = field(
        default_factory=dict
    )

    probe_memory: List[Dict] = field(default_factory=list)

    disclosure_patterns: List[Dict] = field(default_factory=list)

    current_focus: str = "general"

    escalation_level: str = "Low"

    confidence_score: float = 0.0

    narrative_depth_score: float = 0.0

    psychological_profile: Dict = field(
    default_factory=lambda: {

        "distress_level": 0.0,

        "future_orientation_decline": 0.0,

        "functional_withdrawal": 0.0,

        "support_fragility": 0.0,

        "emotional_instability": 0.0,

        "self_harm_risk": 0.0,

        "functional_impairment": 0.0,

        "routine_disruption": 0.0,

        "sleep_disruption": 0.0,

        "concentration_decline": 0.0,

        "motivational_decline": 0.0,

        "social_disconnection": 0.0,

        "persistence_score": 0.0,

        "escalation_score": 0.0,

        "help_openness": 0.5
    }
)