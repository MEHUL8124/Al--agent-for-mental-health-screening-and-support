import os
from pathlib import Path
from dotenv import load_dotenv

# Base directory paths
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = os.getenv("MINDCARE_DB_PATH", str(BASE_DIR / "mindcare_wellness.db"))

# Load .env file
load_dotenv(BASE_DIR / ".env")

# API Keys and Models
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or os.getenv("LLM_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

# Region for Crisis Resources
DEFAULT_REGION = os.getenv("DEFAULT_REGION", "India").strip()

# App Metadata
APP_NAME = "MindCare AI"
APP_TAGLINE = "Understand your patterns. Take your next step."
VERSION = "1.0.0"

# Crisis Resource Contacts (Verified Official Hotlines)
CRISIS_RESOURCES = {
    "India": {
        "emergency": "112 (National Emergency Helpline)",
        "helplines": [
            {
                "name": "Tele-MANAS (Govt of India)",
                "contact": "14416 or 1800-891-4416",
                "details": "24/7 toll-free mental health support across all Indian states and languages.",
                "type": "Toll-Free Phone"
            },
            {
                "name": "KIRAN Helpline",
                "contact": "1800-599-0019",
                "details": "24/7 psychological support provided by the Ministry of Social Justice.",
                "type": "Toll-Free Phone"
            },
            {
                "name": "Vandrevala Foundation",
                "contact": "+91 9999 666 555",
                "details": "Free, confidential 24/7 crisis intervention & counseling.",
                "type": "24/7 Phone & WhatsApp"
            },
            {
                "name": "AASRA",
                "contact": "+91 98204 66726",
                "details": "24/7 suicide prevention and emotional crisis support.",
                "type": "Phone"
            }
        ]
    },
    "United States": {
        "emergency": "911",
        "helplines": [
            {
                "name": "988 Suicide & Crisis Lifeline",
                "contact": "Call or Text 988",
                "details": "24/7, free and confidential support for people in distress.",
                "type": "Phone & Text"
            },
            {
                "name": "The Crisis Text Line",
                "contact": "Text HOME to 741741",
                "details": "Free, 24/7 crisis support via SMS with a trained volunteer.",
                "type": "Text"
            },
            {
                "name": "The Trevor Project (LGBTQ youth)",
                "contact": "1-866-488-7386 or Text START to 678-678",
                "details": "24/7 confidential crisis support for LGBTQ young people.",
                "type": "Phone & Text"
            }
        ]
    },
    "United Kingdom": {
        "emergency": "999",
        "helplines": [
            {
                "name": "Samaritans",
                "contact": "116 123",
                "details": "Free, 24/7 confidential listening service for anyone in need.",
                "type": "Phone"
            },
            {
                "name": "Shout Crisis Text Line",
                "contact": "Text SHOUT to 85258",
                "details": "Free, 24/7 crisis support text line.",
                "type": "Text"
            }
        ]
    },
    "Canada": {
        "emergency": "911",
        "helplines": [
            {
                "name": "988 Suicide Crisis Helpline",
                "contact": "Call or Text 988",
                "details": "Toll-free 24/7 bilingual suicide prevention support across Canada.",
                "type": "Phone & Text"
            }
        ]
    },
    "International / Other": {
        "emergency": "Your local emergency number (e.g. 112, 911, or 999)",
        "helplines": [
            {
                "name": "Befrienders Worldwide",
                "contact": "https://www.befrienders.org",
                "details": "Find confidential, free emotional support services globally.",
                "type": "Online Directory"
            },
            {
                "name": "Find A Helpline (Free, confidential)",
                "contact": "https://findahelpline.com",
                "details": "Directory of support services and crisis helplines in over 130 countries.",
                "type": "Online Directory"
            }
        ]
    }
}
