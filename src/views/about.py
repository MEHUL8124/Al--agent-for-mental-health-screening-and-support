import streamlit as st
from src import config

def render():
    st.title("ℹ️ About MindCare AI, Privacy & Limitations")
    st.caption(f"MindCare AI v{config.VERSION} — An AI Agent for Mental Health Screening and Support")
    
    st.markdown("""
    ### 🎯 Project Purpose
    **MindCare AI** is designed as a production-style academic and portfolio AI engineering project.
    Its mission is to demonstrate how conversational AI, standardized psychological screening frameworks (PHQ-9 and GAD-7),
    and secure personal data tracking can be brought together responsibly with **safety-first architecture**.
    
    ---
    
    ### 🛡️ Ethical Boundaries & Medical Limitations
    1. **Not a Diagnostic Tool**: MindCare AI does **not** diagnose clinical depression, generalized anxiety disorder, bipolar disorder, PTSD, or any other psychiatric illness.
    2. **Not a Medical Device or Therapy Replacement**: Interactions with MindCare AI do not establish a patient-doctor or client-therapist relationship.
    3. **Crisis Priority**: The system incorporates automated heuristic safety filters that intercept expressions of self-harm or suicidal ideation and immediately direct users to human-operated 24/7 crisis hotlines.
    4. **Exploratory NLP**: Sentiment and emotion indicators are surface-level linguistic patterns and should never be used as psychological proof of mental health state.
    
    ---
    
    ### 🔒 Data Privacy & Storage Practices
    - **Local Persistence**: All mood logs, sleep stats, and screening records are stored in a local SQLite file (`mindcare_wellness.db`) residing solely on your personal machine or current execution environment.
    - **No Mandatory Account**: You can use all core features without registering, providing email addresses, or revealing real names.
    - **Complete Data Control**: You can review individual entries, delete single records, or execute a complete data wipe at any time from the **Mood & Wellness Tracker** tab.
    - **Third-Party AI Services**: If configured with an OpenAI API key, conversation prompts are transmitted securely via API to generate empathetic responses; however, local fallback mode operates completely offline without sending any data to external servers.
    
    ---
    
    ### 🛠️ Architecture Stack
    - **Frontend & App Framework**: Streamlit (Python)
    - **Data Processing & Analytics**: Pandas, NumPy
    - **Visualizations**: Plotly Express & Graph Objects
    - **Validation**: Pydantic v2
    - **Safety & NLP**: Rule-based heuristic pattern matching, intent routing, and scikit-learn compatible pipelines
    - **Database**: Parameterized SQLite3
    """)
