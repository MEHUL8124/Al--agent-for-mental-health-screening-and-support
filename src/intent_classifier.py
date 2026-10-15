import re
from typing import Dict, Any

INTENT_KEYWORDS = {
    "crisis": [
        "suicide", "kill myself", "end my life", "want to die", "better off dead",
        "hurt myself", "self harm", "slit", "overdose"
    ],
    "grounding": [
        "panic", "panic attack", "can't breathe", "hyperventilating", "overwhelmed",
        "grounding", "racing heart", "ground me", "calm down"
    ],
    "anxiety": [
        "anxious", "anxiety", "worry", "nervous", "dread", "scared", "fear",
        "racing thoughts", "jittery", "tense", "stress"
    ],
    "depression_sadness": [
        "depressed", "depression", "hopeless", "empty", "crying", "unhappy",
        "sad", "lonely", "worthless", "exhausted", "numb", "miserable"
    ],
    "sleep_trouble": [
        "insomnia", "can't sleep", "sleep", "tired", "nightmare", "waking up",
        "exhausted", "restless"
    ],
    "coping_resources": [
        "technique", "exercise", "breathing", "coping", "help me relax",
        "resource", "therapist", "find help", "counselor"
    ],
    "gratitude_progress": [
        "better today", "feeling good", "proud", "gratitude", "thank you",
        "improving", "happy", "accomplished"
    ]
}

def classify_intent(text: str) -> Dict[str, Any]:
    """
    Classifies user message into primary intent using keyword & rule matching.
    """
    if not text:
        return {"intent": "general_chat", "confidence": 0.5, "keywords_matched": []}
        
    lower_text = text.lower()
    
    # Priority 1: Crisis check
    for kw in INTENT_KEYWORDS["crisis"]:
        if re.search(r"\b" + re.escape(kw) + r"\b", lower_text):
            return {
                "intent": "crisis",
                "confidence": 0.99,
                "keywords_matched": [kw]
            }
            
    # Priority 2: Grounding / Immediate distress
    for kw in INTENT_KEYWORDS["grounding"]:
        if re.search(r"\b" + re.escape(kw) + r"\b", lower_text):
            return {
                "intent": "grounding",
                "confidence": 0.90,
                "keywords_matched": [kw]
            }
            
    # Priority 3: Other categories scoring
    scores = {}
    matched = {}
    for intent, kws in INTENT_KEYWORDS.items():
        if intent in ("crisis", "grounding"):
            continue
        hits = [kw for kw in kws if re.search(r"\b" + re.escape(kw) + r"\b", lower_text)]
        if hits:
            scores[intent] = len(hits)
            matched[intent] = hits
            
    if scores:
        best_intent = max(scores, key=scores.get)
        return {
            "intent": best_intent,
            "confidence": min(0.60 + 0.15 * scores[best_intent], 0.95),
            "keywords_matched": matched[best_intent]
        }
        
    return {
        "intent": "general_chat",
        "confidence": 0.50,
        "keywords_matched": []
    }
