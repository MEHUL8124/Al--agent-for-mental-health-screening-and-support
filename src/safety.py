import re
from typing import Dict, Any, Tuple
from src import config

# Crisis detection keywords and regex patterns
CRISIS_PATTERNS = [
    r"\b(suicide|suicidal|kill\s+myself|end\s+my\s+life|want\s+to\s+die|hang\s+myself|slit\s+my\s+wrist)\b",
    r"\b(better\s+off\s+dead|no\s+reason\s+to\s+live|don't\s+want\s+to\s+wake\s+up|goodbye\s+cruel\s+world)\b",
    r"\b(overdose\s+on\s+pills|jump\s+off\s+a\s+bridge|hurting\s+myself|self\s*harm)\b",
    r"\b(ready\s+to\s+die|planning\s+to\s+die|thinking\s+of\s+ending\s+it\s+all)\b",
]

COMPILED_PATTERNS = [re.compile(p, re.IGNORECASE) for p in CRISIS_PATTERNS]

def check_crisis_indicators(text: str) -> Tuple[bool, str]:
    """
    Evaluates user input for explicit crisis, suicidal ideation, or self-harm keywords.
    Returns (is_crisis_detected, matched_category).
    """
    if not text or not isinstance(text, str):
        return False, ""
    
    clean_text = text.lower().strip()
    
    for pattern in COMPILED_PATTERNS:
        match = pattern.search(clean_text)
        if match:
            return True, f"Crisis indicator matched: '{match.group(0)}'"
            
    return False, ""

def get_crisis_response(region: str = "India") -> Dict[str, Any]:
    """
    Returns an immediate compassionate crisis response with official, verified emergency contacts.
    """
    resources = config.CRISIS_RESOURCES.get(region, config.CRISIS_RESOURCES["India"])
    emergency_num = resources.get("emergency", "112")
    helplines = resources.get("helplines", [])
    
    helpline_text_lines = []
    for h in helplines:
        helpline_text_lines.append(f"- **{h['name']}**: `{h['contact']}` ({h['details']})")
    
    helplines_formatted = "\n".join(helpline_text_lines)
    
    message = f"""### ⚠️ Immediate Support & Safety Resources

It sounds like you are carrying an overwhelming amount of pain right now. **Please know that you do not have to carry this alone, and there is immediate help available.**

Because your safety and life are precious, please reach out right now:

🚨 **Emergency Immediate Assistance:** Call **{emergency_num}** or go to the nearest emergency room.

**Confidential & Free Crisis Helplines ({region}):**
{helplines_formatted}

---
💬 **What you can do right now:**
1. Reach out to a family member, close friend, or someone you trust to be physically with you.
2. If you are in immediate danger of hurting yourself, call emergency services immediately.
3. MindCare AI is an automated self-reflection tool, not a clinical emergency service. Please connect with human crisis specialists who are ready to support you 24/7 without judgment.
"""
    return {
        "is_crisis": True,
        "message": message,
        "region": region,
        "emergency": emergency_num,
        "helplines": helplines
    }
