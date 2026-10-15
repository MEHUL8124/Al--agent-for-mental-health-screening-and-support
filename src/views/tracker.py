import streamlit as st
import pandas as pd
from src import database, validators, text_analysis

def render():
    st.title("📊 Mood & Wellness Tracker")
    st.caption("Record and reflect on your daily patterns in a private, locally stored journal.")
    
    tab_log, tab_history = st.tabs(["📝 New Daily Log", "📜 View & Manage Past Logs"])
    
    with tab_log:
        st.subheader("Log Today's Wellness Metrics")
        
        with st.form("wellness_log_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                mood_score = st.slider(
                    "How is your mood today?",
                    min_value=1,
                    max_value=5,
                    value=3,
                    help="1: Very Low, 2: Low, 3: Neutral, 4: Good, 5: Great"
                )
                mood_labels = {1: "😢 1 - Very Low / Struggling", 2: "🙁 2 - Low / Subdued", 3: "😐 3 - Neutral / Okay", 4: "🙂 4 - Good / Pleasant", 5: "😄 5 - Great / Thriving"}
                st.caption(f"Selected: **{mood_labels[mood_score]}**")
                
                stress_level = st.slider(
                    "Stress Level:",
                    min_value=1,
                    max_value=5,
                    value=2,
                    help="1: Very Low / Relaxed, 5: Extreme / Overwhelmed"
                )
                stress_labels = {1: "🟢 1 - Minimal Stress", 2: "🟡 2 - Manageable", 3: "🟠 3 - Moderate", 4: "🔴 4 - High Stress", 5: "🚨 5 - Overwhelming"}
                st.caption(f"Selected: **{stress_labels[stress_level]}**")
                
            with col2:
                sleep_hours = st.number_input(
                    "Hours of Sleep (past 24h):",
                    min_value=0.0,
                    max_value=24.0,
                    value=7.0,
                    step=0.5
                )
                
                sleep_quality = st.slider(
                    "Sleep Restfulness / Quality:",
                    min_value=1,
                    max_value=5,
                    value=3,
                    help="1: Very Poor / Restless, 5: Deeply Restorative"
                )
                sleep_labels = {1: "😴 1 - Poor / Fitful", 2: "🥱 2 - Restless", 3: "🛌 3 - Moderate", 4: "💤 4 - Restful", 5: "✨ 5 - Deeply Refreshing"}
                st.caption(f"Selected: **{sleep_labels[sleep_quality]}**")

            st.markdown("---")
            st.write("**Activities & Self-Care today (select any):**")
            activities = st.multiselect(
                "Activities",
                ["Exercise / Walk", "Work / Study", "Socializing / Friends", "Outdoors / Nature", "Meditation / Breathing", "Reading", "Hobby / Creative", "Quality Nutrition", "Screen Time / Gaming"],
                default=["Work / Study"],
                label_visibility="collapsed"
            )
            
            journal_text = st.text_area(
                "Optional Journal Reflection (How are you feeling? What's on your mind?):",
                placeholder="Write freely. Your entries are saved strictly to your local machine SQLite database.",
                max_chars=1500
            )
            
            submit_btn = st.form_submit_button("Save Wellness Log", use_container_width=True)
            
        if submit_btn:
            # Validate with Pydantic
            try:
                validated = validators.MoodEntryInput(
                    mood_score=mood_score,
                    stress_level=stress_level,
                    sleep_hours=sleep_hours,
                    sleep_quality=sleep_quality,
                    activities=", ".join(activities),
                    journal_text=journal_text
                )
                
                sentiment_label = ""
                if journal_text.strip():
                    analysis = text_analysis.analyze_reflection_text(journal_text)
                    sentiment_label = analysis["sentiment"]
                    
                database.save_mood_entry(
                    mood_score=validated.mood_score,
                    stress_level=validated.stress_level,
                    sleep_hours=validated.sleep_hours,
                    sleep_quality=validated.sleep_quality,
                    activities=validated.activities,
                    journal_text=validated.journal_text,
                    sentiment_label=sentiment_label
                )
                
                st.success("🎉 Entry successfully saved to your local database!")
                if sentiment_label:
                    st.caption(f"💡 Exploratory linguistic reflection: *{sentiment_label}*")
            except Exception as e:
                st.error(f"Validation Error: {str(e)}")

    with tab_history:
        st.subheader("Your Recorded Wellness Logs")
        entries = database.get_all_mood_entries(limit=100)
        
        if not entries:
            st.info("No recorded logs found yet. Complete a log in the tab above to see your history.")
        else:
            df = pd.DataFrame(entries)
            display_df = df[["id", "timestamp", "mood_score", "stress_level", "sleep_hours", "sleep_quality", "activities", "journal_text"]].copy()
            st.dataframe(display_df, use_container_width=True)
            
            st.markdown("---")
            st.write("### Manage Records")
            col_del_single, col_del_all = st.columns(2)
            
            with col_del_single:
                del_id = st.number_input("Enter Entry ID to delete:", min_value=1, step=1, value=int(entries[0]["id"]))
                if st.button("Delete Specific Entry"):
                    if database.delete_mood_entry(del_id):
                        st.success(f"Entry #{del_id} deleted.")
                        st.rerun()
                    else:
                        st.error("Entry not found.")
                        
            with col_del_all:
                st.write("**Data Privacy & Complete Wipe**")
                confirm = st.checkbox("I confirm I want to wipe ALL my local logs and screening history")
                if st.button("🗑️ Delete All My Data", type="primary"):
                    if confirm:
                        database.delete_all_data()
                        st.success("All data permanently wiped from local database.")
                        st.rerun()
                    else:
                        st.warning("Please check the confirmation box above first.")
