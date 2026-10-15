import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from src import database

def render():
    st.title("📈 Insights & Progress")
    st.caption("Visualizing personal trends across mood, stress, and sleep over time.")
    
    st.info("📊 **Educational Note**: Visual trends reflect your self-reported inputs. Associations between variables (e.g., sleep and stress) do not establish causation, and charts are not clinical predictions.")
    
    entries = database.get_all_mood_entries(limit=100)
    
    if len(entries) < 2:
        st.markdown("""
            <div style="text-align: center; padding: 3rem; background: #F8F9FA; border-radius: 12px; border: 1px dashed #CBD5E0;">
                <h3 style="color: #4A5568;">Not Enough Data Points Yet</h3>
                <p style="color: #718096; max-width: 500px; margin: 0 auto 1.5rem auto;">
                    We need at least <strong>2 recorded daily logs</strong> to plot meaningful trends.
                    Head over to the <strong>Mood & Wellness Tracker</strong> to add entries!
                </p>
            </div>
        """, unsafe_allow_html=True)
        return

    # Convert to DataFrame and sort chronologically
    df = pd.DataFrame(entries)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp")
    
    # 1. Mood & Stress Trend Over Time
    st.subheader("1. Mood & Stress Trajectory")
    fig_trends = go.Figure()
    
    fig_trends.add_trace(go.Scatter(
        x=df["timestamp"],
        y=df["mood_score"],
        mode="lines+markers",
        name="Mood (1=Low, 5=Great)",
        line=dict(color="#2B7A78", width=3),
        marker=dict(size=8)
    ))
    
    fig_trends.add_trace(go.Scatter(
        x=df["timestamp"],
        y=df["stress_level"],
        mode="lines+markers",
        name="Stress (1=Low, 5=High)",
        line=dict(color="#E53E3E", width=3, dash="dot"),
        marker=dict(size=8)
    ))
    
    fig_trends.update_layout(
        title="Mood vs. Stress Over Time",
        xaxis_title="Date / Time",
        yaxis_title="Scale (1 - 5)",
        yaxis=dict(range=[0.5, 5.5], dtick=1),
        template="plotly_white",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig_trends, use_container_width=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    # 2. Sleep Duration vs Mood Relationship
    with col1:
        st.subheader("2. Sleep Duration vs. Mood")
        fig_scatter = px.scatter(
            df,
            x="sleep_hours",
            y="mood_score",
            color="stress_level",
            size="sleep_quality",
            hover_data=["timestamp", "activities"],
            labels={
                "sleep_hours": "Sleep Hours",
                "mood_score": "Mood Score (1-5)",
                "stress_level": "Stress Level",
                "sleep_quality": "Sleep Quality"
            },
            title="Sleep Hours vs. Reported Mood Score",
            template="plotly_white",
            color_continuous_scale="Viridis"
        )
        fig_scatter.update_yaxes(range=[0.5, 5.5], dtick=1)
        st.plotly_chart(fig_scatter, use_container_width=True)
        
    # 3. Sleep Quality Distribution
    with col2:
        st.subheader("3. Sleep Quality Distribution")
        fig_hist = px.histogram(
            df,
            x="sleep_quality",
            nbins=5,
            labels={"sleep_quality": "Sleep Quality (1=Poor, 5=Restorative)"},
            title="Distribution of Sleep Quality Ratings",
            template="plotly_white",
            color_discrete_sequence=["#3AAFA9"]
        )
        fig_hist.update_xaxes(range=[0.5, 5.5], dtick=1)
        st.plotly_chart(fig_hist, use_container_width=True)
        
    # 4. Screening History Summary
    st.markdown("---")
    st.subheader("4. Recent Self-Reflection Screening Summaries")
    screenings = database.get_screening_history(limit=10)
    if screenings:
        sdf = pd.DataFrame(screenings)
        st.dataframe(sdf[["timestamp", "instrument", "total_score", "max_score", "severity"]], use_container_width=True)
    else:
        st.caption("No screening questionnaires completed yet.")
