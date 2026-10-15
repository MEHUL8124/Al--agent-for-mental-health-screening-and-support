import re
from typing import Dict, Any

# Lexicons for lightweight, transparent rule-based text exploration
POSITIVE_WORDS = {
    "happy", "calm", "grateful", "peaceful", "relaxed", "better", "improving",
    "hopeful", "relieved", "strong", "good", "great", "content", "joy", "supported"
}

NEGATIVE_WORDS = {
    "sad", "depressed", "anxious", "overwhelmed", "hopeless", "exhausted",
    "tired", "stressed", "worthless", "angry", "lonely", "numb", "scared", "fear"
}

EMOTION_THEMES = {
    "Overwhelmed / High Stress": ["overwhelmed", "drowning", "too much", "pressure", "burnout", "exploding"],
    "Anxious / Apprehensive": ["worry", "panic", "nervous", "scared", "anxious", "tense", "dread"],
    "Low Energy / Depleted": ["exhausted", "tired", "drained", "no energy", "fatigued", "heavy"],
    "Sadness / Grief": ["crying", "empty", "sad", "unhappy", "grief", "loss", "lonely"],
    "Calm / Hopeful": ["calm", "better", "hope", "peaceful", "progress", "coping", "fine"]
}

def analyze_reflection_text(text: str) -> Dict[str, Any]:
    """
    Analyzes journal or reflection text for educational linguistic exploration.
    IMPORTANT: This is not a clinical assessment or psychological diagnosis.
    """
    if not text or not text.strip():
        return {
            "word_count": 0,
            "sentiment": "Neutral / Undetermined",
            "score": 0.0,
            "emotions_detected": [],
            "disclaimer": "Linguistic analysis is exploratory and should never be considered a psychological evaluation."
        }
        
    words = re.findall(r"\b\w+\b", text.lower())
    total_words = len(words)
    
    pos_count = sum(1 for w in words if w in POSITIVE_WORDS)
    neg_count = sum(1 for w in words if w in NEGATIVE_WORDS)
    
    diff = pos_count - neg_count
    norm_score = max(-1.0, min(1.0, diff / max(total_words, 1) * 3))
    
    if diff > 1:
        sentiment = "Predominantly Positive / Calming"
    elif diff < -1:
        sentiment = "Elevated Stress / Lower Tone"
    else:
        sentiment = "Balanced / Neutral"
        
    detected_emotions = []
    lower_text = text.lower()
    for theme, keywords in EMOTION_THEMES.items():
        matched = [k for k in keywords if re.search(r"\b" + re.escape(k) + r"\b", lower_text)]
        if matched:
            detected_emotions.append({
                "theme": theme,
                "keywords": matched
            })
            
    return {
        "word_count": total_words,
        "sentiment": sentiment,
        "sentiment_score": round(norm_score, 2),
        "positive_word_count": pos_count,
        "negative_word_count": neg_count,
        "emotions_detected": detected_emotions,
        "disclaimer": "Notice: This linguistic reflection reflects surface-level word patterns for your personal journaling context and is not a clinical assessment."
    }
