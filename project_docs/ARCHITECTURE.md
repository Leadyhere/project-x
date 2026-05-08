# SYSTEM ARCHITECTURE

# Core Architecture Philosophy

The architecture follows:
- privacy-first design
- listening-first conversational flow
- rule-based safety enforcement
- modular cognitive engines

The system separates:
1. Conversational intelligence
2. Safety decision making

This prevents:
- unsafe LLM autonomy
- hallucinated risk assessments
- emotionally manipulative behavior

---

# HIGH LEVEL ARCHITECTURE

Frontend
    ↓
FastAPI API Layer
    ↓
Session Manager
    ↓
Conversation Orchestrator
    ↓
Cognitive Analysis Engines
    ↓
Safety & Confidence Engines
    ↓
Dynamic Response Generator
    ↓
Narrative Summary Generator

---

# CORE COMPONENTS

## 1. Session Layer

File:
- session_model.py

Responsibilities:
- user session state
- psychological profile
- conversation memory
- topic tracking
- investigation queue
- coping pattern storage
- support pattern storage
- confidence tracking

---

## 2. Conversation Orchestrator

File:
- conversation_orchestrator.py

Responsibilities:
- central conversational control
- engine coordination
- dynamic questioning
- adaptive routing
- safety orchestration

This is the brain of the backend.

---

## 3. NLP Analyzer

File:
- nlp_analyzer.py

Responsibilities:
- topic extraction
- emotional signal detection
- semantic understanding
- distress detection

---

## 4. Psychological State Engine

File:
- psychological_state_engine.py

Responsibilities:
- cognitive state modeling
- distress accumulation
- future orientation decline tracking
- social disconnection tracking
- motivational decline tracking

---

## 5. Investigation Planner

File:
- investigation_planner.py

Responsibilities:
- decide what requires deeper exploration
- dynamically change conversation direction
- prioritize safety-sensitive themes

---

## 6. Coverage System

Files:
- coverage_tracker.py
- semantic_coverage_engine.py

Responsibilities:
- detect already-covered psychological areas
- avoid repetitive questioning
- infer indirect answers

---

## 7. Risk System

Files:
- risk_engine.py
- semantic_risk_engine.py

Responsibilities:
- risk classification
- suicidal signal detection
- escalation priority

Risk engine is rule-based only.

---

## 8. Confidence Engine

File:
- confidence_engine.py

Responsibilities:
- estimate reliability of assessment
- prevent overconfidence
- measure narrative completeness

---

## 9. Narrative Engines

Files:
- narrative_depth_engine.py
- reflection_engine.py
- narrative_summary_engine.py

Responsibilities:
- narrative richness detection
- psychological reflection
- longitudinal summary creation

---

## 10. Behavioral Pattern Engines

Files:
- coping_engine.py
- support_engine.py
- contradiction_engine.py
- drift_engine.py

Responsibilities:
- coping style detection
- support reliability understanding
- emotional inconsistency detection
- emotional drift analysis

---

# CURRENT FLOW

User Message
    ↓
Conversation Orchestrator
    ↓
NLP Analysis
    ↓
Coverage Detection
    ↓
Psychological State Update
    ↓
Drift Detection
    ↓
Contradiction Detection
    ↓
Investigation Planning
    ↓
Risk Evaluation
    ↓
Confidence Scoring
    ↓
Dynamic Question Generation
    ↓
Response Returned

---

# PRIVACY ARCHITECTURE

Current philosophy:
- ephemeral sessions
- temporary memory
- no permanent raw conversation storage

Future production architecture:
Session
    ↓
Assessment Generation
    ↓
Optional PDF Export
    ↓
Conversation Deletion
    ↓
Retain Anonymized Learning Metrics Only

---

# FUTURE ARCHITECTURE GOALS

## Multimodal Layer
Future additions:
- voice emotion analysis
- hesitation detection
- silence analysis
- speech speed analysis
- tone fluctuation analysis

## AI Twin Layer
Future additions:
- longitudinal emotional memory
- behavioral persistence modeling
- motivational structure tracking
- emotional evolution mapping
- cognitive pattern simulation

## Retrieval Layer
Future:
- semantic memory retrieval
- vector database integration
- contextual narrative recall