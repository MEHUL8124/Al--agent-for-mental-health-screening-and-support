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

# Session state initialization for theme
if "dark_mode" not in st.session_state:
    st.session_state["dark_mode"] = False

is_dark = st.session_state["dark_mode"]

# Dynamic CSS Theme Injection
if is_dark:
    theme_css = """
    <style>
        /* Dark Theme Variables */
        :root {
            --bg-main: #0B1120;
            --bg-surface: #1E293B;
            --bg-card: #1E293B;
            --border-color: #334155;
            --text-primary: #F8FAFC;
            --text-secondary: #94A3B8;
            --accent-primary: #2DD4BF;
            --accent-secondary: #38BDF8;
        }

        /* App Background & Base Typography */
        .stApp {
            background-color: #0B1120 !important;
            color: #F8FAFC !important;
        }
        
        /* Sidebar Styling */
        section[data-testid="stSidebar"] {
            background-color: #070D18 !important;
            border-right: 1px solid #1E293B !important;
        }
        section[data-testid="stSidebar"] * {
            color: #F8FAFC !important;
        }
        
        /* Metric Cards */
        div[data-testid="stMetricValue"] {
            font-weight: 700;
            color: #2DD4BF !important;
        }
        div[data-testid="stMetricLabel"] {
            color: #94A3B8 !important;
        }

        /* Custom Cards & Empty States */
        .custom-card {
            background: #1E293B !important;
            border: 1px solid #334155 !important;
            color: #F8FAFC !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3) !important;
        }
        .custom-card h4 {
            color: #2DD4BF !important;
        }
        .custom-card p {
            color: #94A3B8 !important;
        }
        .custom-empty-card {
            background: #141E33 !important;
            border: 1px dashed #334155 !important;
            color: #94A3B8 !important;
        }
        .custom-empty-card h3, .custom-empty-card h4 {
            color: #E2E8F0 !important;
        }

        /* Input Controls, Selectboxes & Textareas */
        .stTextInput>div>div>input, 
        .stTextArea>div>div>textarea, 
        .stSelectbox>div>div,
        .stNumberInput>div>div>input {
            background-color: #1E293B !important;
            color: #F8FAFC !important;
            border: 1px solid #334155 !important;
        }
        
        /* Buttons */
        .stButton>button {
            background-color: #1E293B !important;
            color: #F8FAFC !important;
            border: 1px solid #334155 !important;
            border-radius: 8px;
            transition: all 0.2s ease-in-out;
        }
        .stButton>button:hover {
            border-color: #2DD4BF !important;
            color: #2DD4BF !important;
            box-shadow: 0 0 10px rgba(45, 212, 191, 0.2) !important;
        }

        /* Streamlit Tabs */
        .stTabs [data-baseweb="tab-list"] {
            background-color: #0B1120 !important;
            border-bottom: 1px solid #1E293B !important;
        }
        .stTabs [data-baseweb="tab"] {
            color: #94A3B8 !important;
        }
        .stTabs [aria-selected="true"] {
            color: #2DD4BF !important;
            border-bottom-color: #2DD4BF !important;
        }
        
        /* Expanders */
        .streamlit-expanderHeader {
            background-color: #1E293B !important;
            color: #F8FAFC !important;
            border: 1px solid #334155 !important;
        }
        .streamlit-expanderContent {
            background-color: #141E33 !important;
            border: 1px solid #334155 !important;
            border-top: none !important;
        }

        /* Dataframe styling */
        div[data-testid="stDataFrame"] {
            border: 1px solid #334155 !important;
            border-radius: 8px;
        }

        /* Typography */
        h1, h2, h3, h4, h5, h6 {
            color: #F8FAFC !important;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }
        p, span, label {
            color: #CBD5E1;
        }
    </style>
    """
else:
    theme_css = """
    <style>
        /* Light Theme Styles */
        .stApp {
            background-color: #F8F9FD !important;
            color: #17252A !important;
        }
        section[data-testid="stSidebar"] {
            background-color: #FFFFFF !important;
            border-right: 1px solid #E2E8F0 !important;
        }
        div[data-testid="stMetricValue"] {
            font-weight: 700;
            color: #2B7A78 !important;
        }
        div[data-testid="stMetricLabel"] {
            color: #4A5568 !important;
        }
        .custom-card {
            background: #FFFFFF !important;
            border: 1px solid #E2E8F0 !important;
            color: #17252A !important;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
        }
        .custom-card h4 {
            color: #2B7A78 !important;
        }
        .custom-card p {
            color: #4A5568 !important;
        }
        .custom-empty-card {
            background: #F8F9FA !important;
            border: 1px dashed #CBD5E0 !important;
            color: #A0AEC0 !important;
        }
        .custom-empty-card h3, .custom-empty-card h4 {
            color: #4A5568 !important;
        }
        .stButton>button {
            border-radius: 8px;
            transition: all 0.2s ease-in-out;
        }
        .stButton>button:hover {
            border-color: #2B7A78 !important;
            color: #2B7A78 !important;
        }
        h1, h2, h3, h4, h5, h6 {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }
    </style>
    """

st.markdown(theme_css, unsafe_allow_html=True)

# Sidebar Navigation & Settings
with st.sidebar:
    st.markdown("## 🌿 MindCare AI")
    st.caption("AI-Assisted Mental Wellness Screening & Support")
    
    # Dark Mode Toggle
    dark_mode_val = st.toggle("🌙 Dark Mode", value=is_dark, key="theme_toggle")
    if dark_mode_val != is_dark:
        st.session_state["dark_mode"] = dark_mode_val
        st.rerun()
        
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
