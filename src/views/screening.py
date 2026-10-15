import streamlit as st
from src import screening, database, safety, config

def render():
    st.title("📋 Mental Wellness Screening")
    st.caption("Standardized self-reflection questionnaires for symptom awareness.")
    
    st.warning("⚠️ **Important Disclaimer**: These questionnaires (PHQ-9 and GAD-7) are preliminary screening and self-reflection tools used widely in healthcare settings, but they **do not provide a clinical diagnosis**. A formal diagnosis can only be made by a qualified healthcare professional.")
    
    instrument = st.selectbox(
        "Choose Screening Instrument:",
        ["PHQ-9 (Depression & Low Mood Symptoms)", "GAD-7 (Anxiety & Worry Symptoms)"]
    )
    
    st.markdown("---")
    
    if "PHQ-9" in instrument:
        render_phq9()
    else:
        render_gad7()

def render_phq9():
    st.subheader("PHQ-9: Patient Health Questionnaire-9")
    st.write("*Over the last 2 weeks, how often have you been bothered by any of the following problems?*")
    
    scale_options = [
        "0 - Not at all",
        "1 - Several days",
        "2 - More than half the days",
        "3 - Nearly every day"
    ]
    
    with st.form("phq9_form"):
        answers = []
        for i, q in enumerate(screening.PHQ9_QUESTIONS):
            # Special highlighting for Question 9
            if i == 8:
                st.markdown(f"**{q}** *(Safety sensitive item)*")
            else:
                st.markdown(f"**{q}**")
            val = st.radio(
                f"Select response for Item {i+1}",
                scale_options,
                index=0,
                key=f"phq9_q_{i}",
                label_visibility="collapsed"
            )
            score_num = int(val[0])
            answers.append(score_num)
            st.write("")
            
        submitted = st.form_submit_button("Calculate & Review PHQ-9 Result", use_container_width=True)
        
    if submitted:
        result = screening.score_phq9(answers)
        st.markdown("---")
        st.subheader("📊 Your Screening Summary")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total PHQ-9 Score", f"{result['total_score']} / 27")
        with col2:
            st.metric("Severity Category", result["severity"])
            
        st.info(f"**Interpretation & Guidance**: {result['guidance']}")
        
        # Critical Safety Trigger: Question 9
        if result["safety_alert"]:
            st.error("🚨 **Safety Alert Regarding Self-Harm Ideation**")
            st.markdown("""
                You indicated having thoughts related to hurting yourself or being better off dead.
                **Your life matters, and support is available right now.** Please reach out immediately:
            """)
            region = st.session_state.get("selected_region", config.DEFAULT_REGION)
            crisis_info = safety.get_crisis_response(region)
            st.markdown(crisis_info["message"])
            
        # Save to local database
        database.save_screening_result(
            instrument="PHQ-9",
            total_score=result["total_score"],
            max_score=result["max_score"],
            severity=result["severity"],
            safety_alert=result["safety_alert"]
        )
        st.success("✅ Screening result saved to your private local history.")

def render_gad7():
    st.subheader("GAD-7: Generalized Anxiety Disorder 7-item")
    st.write("*Over the last 2 weeks, how often have you been bothered by the following problems?*")
    
    scale_options = [
        "0 - Not at all",
        "1 - Several days",
        "2 - More than half the days",
        "3 - Nearly every day"
    ]
    
    with st.form("gad7_form"):
        answers = []
        for i, q in enumerate(screening.GAD7_QUESTIONS):
            st.markdown(f"**{q}**")
            val = st.radio(
                f"Select response for Item {i+1}",
                scale_options,
                index=0,
                key=f"gad7_q_{i}",
                label_visibility="collapsed"
            )
            score_num = int(val[0])
            answers.append(score_num)
            st.write("")
            
        submitted = st.form_submit_button("Calculate & Review GAD-7 Result", use_container_width=True)
        
    if submitted:
        result = screening.score_gad7(answers)
        st.markdown("---")
        st.subheader("📊 Your Screening Summary")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total GAD-7 Score", f"{result['total_score']} / 21")
        with col2:
            st.metric("Severity Category", result["severity"])
            
        st.info(f"**Interpretation & Guidance**: {result['guidance']}")
        
        # Save to local database
        database.save_screening_result(
            instrument="GAD-7",
            total_score=result["total_score"],
            max_score=result["max_score"],
            severity=result["severity"],
            safety_alert=False
        )
        st.success("✅ Screening result saved to your private local history.")
