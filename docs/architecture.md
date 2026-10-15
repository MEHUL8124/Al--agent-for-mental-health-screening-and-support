# MindCare AI Architecture Documentation

## 1. System Overview
**MindCare AI** is an AI-assisted mental wellness application providing structured self-reflection screening (PHQ-9, GAD-7), daily mood & wellness logging, interactive analytics, evidence-informed coping exercises, and safe conversational support.

```
                           +-------------------------------------+
                           |          Streamlit Frontend         |
                           |  (Navigation Router: app.py, Views) |
                           +------------------+------------------+
                                              |
                     +------------------------+------------------------+
                     |                        |                        |
           +---------v---------+    +---------v---------+    +---------v---------+
           | Screening Module  |    | AI Support Agent  |    | Mood & Wellness   |
           | (PHQ-9 & GAD-7)   |    | Pipeline          |    | Tracker           |
           +---------+---------+    +---------+---------+    +---------+---------+
                     |                        |                        |
                     |              +---------v---------+              |
                     |              |   Safety Engine   |              |
                     |              | (Crisis Override) |              |
                     |              +---------+---------+              |
                     |                        |                        |
                     |              +---------v---------+              |
                     |              | Hybrid Response:  |              |
                     |              | - LLM API         |              |
                     |              | - CBT Engine      |              |
                     +------------------------+------------------------+
                                              |
                                    +---------v---------+
                                    | SQLite Data Layer |
                                    | (Local Persistent)|
                                    +-------------------+
```

## 2. Core Modules
- **`app.py`**: Streamlit entry point, custom UI styles, persistent session state routing.
- **`src/views/`**: Modular presentation views (`home`, `screening`, `chat`, `tracker`, `insights`, `resources`, `about`).
- **`src/screening.py`**: Implementation of standardized PHQ-9 (9 items) and GAD-7 (7 items) scoring algorithms, severity classifications, and Item 9 self-harm safety trigger.
- **`src/safety.py`**: Heuristic keyword & regex pattern safety layer with verified emergency hotlines for India, US, UK, Canada, and International.
- **`src/agent.py`**: AI conversation orchestrator that enforces safety overrides first, classifies user intent, calls LLM if API key is present, and falls back to deterministic empathetic CBT responses if offline.
- **`src/intent_classifier.py`**: Multiclass intent classification for anxiety, low mood, grounding, sleep trouble, coping resources, and crisis.
- **`src/text_analysis.py`**: Exploratory NLP sentiment & emotional tone analysis.
- **`src/response_engine.py`**: Deterministic supportive CBT-informed response templates (5-4-3-2-1 grounding, Box breathing, cognitive reframing).
- **`src/resource_service.py`**: Curated directory of evidence-based self-regulation techniques and guide to finding licensed mental health professionals.
- **`src/database.py`**: Parameterized SQLite database manager ensuring zero SQL injection risk.
- **`src/validators.py`**: Pydantic schemas validating all user inputs.
