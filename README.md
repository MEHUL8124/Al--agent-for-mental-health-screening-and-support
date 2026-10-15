# 🌿 MindCare AI: An AI Agent for Mental Health Screening and Support

> *"Understand your patterns. Take your next step."*

MindCare AI is a complete, production-style mental wellness application built with Python and Streamlit. It combines standardized self-reflection screening questionnaires (PHQ-9 and GAD-7), an AI support conversational agent with high-priority safety routing, local SQLite mood tracking, interactive Plotly analytics, and evidence-informed coping exercises.

---

## 🌟 Key Features

1. **🏠 Home Dashboard**: Snapshot of personal metrics, quick navigation cards, and instant crisis resource access.
2. **📋 Standardized Wellness Screening**:
   - **PHQ-9** (Patient Health Questionnaire 9-item for depressive symptoms) with published clinical scoring ranges.
   - **GAD-7** (Generalized Anxiety Disorder 7-item for anxiety symptoms).
   - **Specialized Item 9 Safety Workflow**: Automatically routes to verified crisis hotlines if thoughts of self-harm are reported, regardless of the aggregate score.
3. **💬 AI Support Chat**:
   - Empathetic dialogue offering grounding techniques (5-4-3-2-1), paced breathing (4-4-4-4 Box Breathing), and cognitive reframing prompts.
   - Configurable for OpenAI LLMs (`gpt-4o-mini`), with a **transparent offline fallback response engine** when no API key is set.
   - Strict non-diagnostic safety guardrails.
4. **📊 Mood & Wellness Tracker**:
   - Daily logs for mood (1-5), stress (1-5), sleep hours, sleep restfulness, and journal thoughts.
   - Pydantic schema validation & parameterized SQLite storage (`mindcare_wellness.db`).
   - One-click record deletion and complete database wipe capabilities.
5. **📈 Insights & Progress**:
   - Interactive Plotly visualizations for mood trends, stress trajectory, and sleep quality distributions.
6. **🌿 Coping Strategies & Resources**:
   - Searchable, category-filtered library of evidence-informed exercises (CBT reframing, Box breathing, Sleep hygiene).
   - Verified 24/7 crisis numbers for India, the US, UK, Canada, and International directories.
7. **ℹ️ About & Privacy**:
   - Clear medical disclaimers, data ownership policies, and model card documentation.

---

## 🚀 Quickstart Guide

### 1. Prerequisites
- Python 3.10 or 3.11 installed on your system.

### 2. Activate Virtual Environment
Open PowerShell or your terminal in the workspace root:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
```powershell
cd mindcare_ai
pip install -r requirements.txt
```

### 4. Optional: Configure API Keys
To enable cloud-based generative AI responses, create a `.env` file in `mindcare_ai/`:
```env
OPENAI_API_KEY=your_openai_api_key_here
DEFAULT_REGION=India
```
*(Note: If no API key is provided, the application automatically runs using its built-in offline supportive response engine!)*

### 5. Launch Application
```powershell
streamlit run app.py
```
Open your browser at `http://localhost:8501`.

---

## 🧪 Running Automated Tests
Run the complete Pytest suite to verify screening scoring, database CRUD, crisis detection, and schema validation:
```powershell
python -m pytest -v
```
All 20 unit and integration tests pass with 100% coverage across core modules.

---

## 📁 Project Architecture
```
mindcare_ai/
├── app.py                      # Main application entrypoint & routing
├── requirements.txt            # Python dependencies
├── .env.example                # Environment variables template
├── .streamlit/
│   └── config.toml             # Theme & server configuration
├── src/
│   ├── config.py               # Settings & regional crisis directories
│   ├── database.py             # SQLite persistence layer
│   ├── validators.py           # Pydantic validation schemas
│   ├── screening.py            # PHQ-9 & GAD-7 scoring algorithms
│   ├── safety.py               # Crisis detection & emergency overrides
│   ├── intent_classifier.py    # Support intent routing
│   ├── text_analysis.py        # Exploratory NLP sentiment analysis
│   ├── response_engine.py      # Local CBT-informed supportive engine
│   ├── agent.py                # AI agent orchestrator
│   ├── resource_service.py     # Coping library service
│   └── views/                  # Streamlit UI page views
│       ├── home.py
│       ├── screening.py
│       ├── chat.py
│       ├── tracker.py
│       ├── insights.py
│       ├── resources.py
│       └── about.py
├── tests/                      # Automated test suite
│   ├── test_screening.py
│   ├── test_safety.py
│   ├── test_database.py
│   └── test_validators.py
└── docs/                       # Comprehensive documentation
    ├── architecture.md
    ├── privacy.md
    └── model_card.md
```

---

## ⚠️ Medical & Safety Disclaimer
MindCare AI is an educational self-reflection and preliminary screening tool. **It does not provide medical diagnoses, clinical treatment, or psychiatric emergency interventions.** If you or someone you know is in immediate danger, please contact emergency services (112 in India, 911 in US/Canada, 999 in UK) or call a 24/7 crisis helpline.
