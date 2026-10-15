import sys
from pathlib import Path
import streamlit as st

# Ensure base project directory is in sys.path
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from src import config, database
from src.views import home, screening, chat, tracker, insights, resources, about

# Initialize local SQLite database tables
database.init_db()

# Streamlit Page Configuration
st.set_page_config(
    page_title="MindCare AI — Mental Health Screening & Support",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for polished aesthetic
st.markdown("""
<style>
    /* Metric Card Styling */
    div[data-testid="stMetricValue"] {
        font-weight: 700;
        color: #2B7A78;
    }
    /* Buttons */
    .stButton>button {
        border-radius: 8px;
        transition: all 0.2s ease-in-out;
    }
    .stButton>button:hover {
        border-color: #2B7A78;
        color: #2B7A78;
    }
    /* Clean headers */
    h1, h2, h3 {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation & Settings
with st.sidebar:
    st.markdown("## 🌿 MindCare AI")
    st.caption("AI-Assisted Mental Wellness Screening & Support")
    st.markdown("---")
    
    # Navigation options
    PAGES = [
        "🏠 Home Dashboard",
        "📋 Mental Wellness Screening",
        "💬 AI Support Chat",
        "📊 Mood & Wellness Tracker",
        "📈 Insights & Progress",
        "🌿 Coping Strategies & Resources",
        "ℹ️ About, Privacy & Limitations"
    ]
    
    # Check if a page was programmatically requested (e.g. from Home buttons)
    if "nav_selection" in st.session_state:
        # Match by name substring
        for p in PAGES:
            if st.session_state["nav_selection"] in p:
                st.session_state["active_nav"] = p
                break
        del st.session_state["nav_selection"]
        
    current_page = st.session_state.get("active_nav", PAGES[0])
    selected_page = st.radio(
        "Navigation",
        PAGES,
        index=PAGES.index(current_page) if current_page in PAGES else 0,
        key="active_nav"
    )
    
    st.markdown("---")
    st.markdown("### 📍 Crisis Support Region")
    region_options = list(config.CRISIS_RESOURCES.keys())
    selected_region = st.selectbox(
        "Select your region for helplines:",
        region_options,
        index=region_options.index("India") if "India" in region_options else 0,
        key="selected_region"
    )
    
    st.markdown("---")
    st.caption(f"MindCare AI v{config.VERSION}")
    st.caption("🔒 All data saved locally on this device.")

# Router
if "Home Dashboard" in selected_page:
    home.render()
elif "Mental Wellness Screening" in selected_page:
    screening.render()
elif "AI Support Chat" in selected_page:
    chat.render()
elif "Mood & Wellness Tracker" in selected_page:
    tracker.render()
elif "Insights & Progress" in selected_page:
    insights.render()
elif "Coping Strategies & Resources" in selected_page:
    resources.render()
elif "About, Privacy & Limitations" in selected_page:
    about.render()
