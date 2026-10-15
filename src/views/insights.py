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
            <div class="custom-empty-card" style="text-align: center; padding: 3rem; border-radius: 12px;">
                <h3>Not Enough Data Points Yet</h3>
                <p style="max-width: 500px; margin: 0 auto 1.5rem auto;">
                    We need at least <strong>2 recorded daily logs</strong> to plot meaningful trends.
                    Head over to the <strong>Mood & Wellness Tracker</strong> to add entries!
                </p>
            </div>
        """, unsafe_allow_html=True)
        return

    is_dark = st.session_state.get("dark_mode", False)
    plot_template = "plotly_dark" if is_dark else "plotly_white"
    bg_color = "#1E293B" if is_dark else "#FFFFFF"
    font_color = "#F8FAFC" if is_dark else "#17252A"

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
        line=dict(color="#2DD4BF" if is_dark else "#2B7A78", width=3),
        marker=dict(size=8)
    ))
    
    fig_trends.add_trace(go.Scatter(
        x=df["timestamp"],
        y=df["stress_level"],
        mode="lines+markers",
        name="Stress (1=Low, 5=High)",
        line=dict(color="#F87171" if is_dark else "#E53E3E", width=3, dash="dot"),
        marker=dict(size=8)
    ))
    
    fig_trends.update_layout(
        title="Mood vs. Stress Over Time",
        xaxis_title="Date / Time",
        yaxis_title="Scale (1 - 5)",
        yaxis=dict(range=[0.5, 5.5], dtick=1),
        template=plot_template,
        paper_bgcolor=bg_color,
        plot_bgcolor=bg_color,
        font=dict(color=font_color),
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
            template=plot_template,
            color_continuous_scale="Viridis"
        )
        fig_scatter.update_layout(
            paper_bgcolor=bg_color,
            plot_bgcolor=bg_color,
            font=dict(color=font_color)
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
            template=plot_template,
            color_discrete_sequence=["#2DD4BF" if is_dark else "#3AAFA9"]
        )
        fig_hist.update_layout(
            paper_bgcolor=bg_color,
            plot_bgcolor=bg_color,
            font=dict(color=font_color)
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
