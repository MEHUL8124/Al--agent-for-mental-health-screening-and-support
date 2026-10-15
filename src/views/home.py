import streamlit as st
import pandas as pd
from src import database, config

def render():
    is_dark = st.session_state.get("dark_mode", False)
    hero_grad = (
        "linear-gradient(135deg, #134E4A 0%, #0F172A 100%)"
        if is_dark
        else "linear-gradient(135deg, #2B7A78 0%, #17252A 100%)"
    )
    
    st.markdown(f"""
        <div style="background: {hero_grad}; padding: 2.2rem; border-radius: 16px; color: white; margin-bottom: 2rem; border: 1px solid {'#334155' if is_dark else 'transparent'};">
            <h1 style="color: white; margin: 0; font-size: 2.4rem;">MindCare AI</h1>
            <p style="font-size: 1.15rem; opacity: 0.9; margin: 0.5rem 0 1rem 0;">
                <em>"Understand your patterns. Take your next step."</em>
            </p>
            <p style="font-size: 0.95rem; line-height: 1.5; margin: 0; max-width: 780px; opacity: 0.85;">
                An AI-assisted mental wellness companion providing structured self-reflection screening,
                evidence-informed coping exercises, daily wellness tracking, and supportive dialogue.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.info("ℹ️ **Notice & Boundaries**: MindCare AI is an educational self-reflection and preliminary wellness tool. It **does not provide medical diagnoses**, clinical evaluations, or emergency care.")
    
    # Quick Navigation Cards
    st.subheader("⚡ Quick Actions")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="custom-card" style="border-radius: 12px; padding: 1.2rem; min-height: 175px;">
                <h4 style="margin: 0;">📋 Wellness Screening</h4>
                <p style="font-size: 0.88rem; margin-top: 0.4rem;">
                    Validated PHQ-9 (mood) and GAD-7 (anxiety) structured self-reflection questionnaires with transparent scoring.
                </p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Start Screening →", key="btn_nav_screen", use_container_width=True):
            st.session_state["nav_selection"] = "Mental Wellness Screening"
            st.rerun()

    with col2:
        st.markdown("""
            <div class="custom-card" style="border-radius: 12px; padding: 1.2rem; min-height: 175px;">
                <h4 style="margin: 0;">💬 AI Support Chat</h4>
                <p style="font-size: 0.88rem; margin-top: 0.4rem;">
                    Empathetic conversation offering sensory grounding (5-4-3-2-1), paced breathing, and mindful reflection.
                </p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Open Support Chat →", key="btn_nav_chat", use_container_width=True):
            st.session_state["nav_selection"] = "AI Support Chat"
            st.rerun()

    with col3:
        st.markdown("""
            <div class="custom-card" style="border-radius: 12px; padding: 1.2rem; min-height: 175px;">
                <h4 style="margin: 0;">📊 Daily Tracker</h4>
                <p style="font-size: 0.88rem; margin-top: 0.4rem;">
                    Log your daily mood, stress level, sleep duration, and journal thoughts securely stored on your device.
                </p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Log Today's Mood →", key="btn_nav_tracker", use_container_width=True):
            st.session_state["nav_selection"] = "Mood & Wellness Tracker"
            st.rerun()

    st.markdown("---")
    
    # Recent Summary & Empty State Handling
    st.subheader("📈 Recent Wellness Snapshot")
    entries = database.get_all_mood_entries(limit=5)
    
    if not entries:
        st.markdown("""
            <div class="custom-empty-card" style="text-align: center; padding: 2.5rem; border-radius: 12px;">
                <h4 style="margin-bottom: 0.5rem;">No wellness entries recorded yet</h4>
                <p style="font-size: 0.95rem; margin-bottom: 1.2rem;">
                    Your wellness journey starts with your first log. Take 60 seconds to record how you're feeling today!
                </p>
            </div>
        """, unsafe_allow_html=True)
    else:
        df = pd.DataFrame(entries)
        latest = entries[0]
        
        stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)
        mood_emojis = {1: "😢 Very Low (1/5)", 2: "🙁 Low (2/5)", 3: "😐 Neutral (3/5)", 4: "🙂 Good (4/5)", 5: "😄 Great (5/5)"}
        
        with stat_col1:
            st.metric("Latest Mood", mood_emojis.get(latest['mood_score'], f"{latest['mood_score']}/5"))
        with stat_col2:
            st.metric("Latest Stress Level", f"{latest['stress_level']} / 5")
        with stat_col3:
            st.metric("Sleep Last Night", f"{latest['sleep_hours']} hrs")
        with stat_col4:
            st.metric("Total Entries Logged", len(entries))
            
        st.caption(f"Last logged: {latest['timestamp']}")
        
    st.markdown("---")
    
    # Crisis Helplines Quick Access
    with st.expander("🚨 Need immediate crisis support? Click to view 24/7 verified emergency numbers"):
        region = st.session_state.get("selected_region", config.DEFAULT_REGION)
        info = config.CRISIS_RESOURCES.get(region, config.CRISIS_RESOURCES["India"])
        st.error(f"**Emergency Immediate Response**: Dial **{info['emergency']}**")
        st.markdown(f"**Verified 24/7 Helplines ({region}):**")
        for h in info["helplines"]:
            st.write(f"- **{h['name']}**: `{h['contact']}` — *{h['details']}*")
