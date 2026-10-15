from typing import List, Dict, Any, Tuple

# PHQ-9: Patient Health Questionnaire-9
PHQ9_QUESTIONS = [
    "1. Little interest or pleasure in doing things",
    "2. Feeling down, depressed, or hopeless",
    "3. Trouble falling or staying asleep, or sleeping too much",
    "4. Feeling tired or having little energy",
    "5. Poor appetite or overeating",
    "6. Feeling bad about yourself — or that you are a failure or have let yourself or your family down",
    "7. Trouble concentrating on things, such as reading the newspaper or watching television",
    "8. Moving or speaking so slowly that other people could have noticed? Or the opposite — being so fidgety or restless that you have been moving around a lot more than usual",
    "9. Thoughts that you would be better off dead or of hurting yourself in some way"
]

# GAD-7: Generalized Anxiety Disorder 7-item
GAD7_QUESTIONS = [
    "1. Feeling nervous, anxious, or on edge",
    "2. Not being able to stop or control worrying",
    "3. Worrying too much about different things",
    "4. Trouble relaxing",
    "5. Being so restless that it is hard to sit still",
    "6. Becoming easily annoyed or irritable",
    "7. Feeling afraid as if something awful might happen"
]

RESPONSE_SCALE = [
    ("Not at all", 0),
    ("Several days", 1),
    ("More than half the days", 2),
    ("Nearly every day", 3)
]

def score_phq9(answers: List[int]) -> Dict[str, Any]:
    """
    Computes PHQ-9 score, severity level, and flags Question 9 safety trigger.
    Score range: 0 to 27.
    """
    if len(answers) != 9:
        raise ValueError(f"PHQ-9 requires exactly 9 responses. Received: {len(answers)}")
    
    total = sum(answers)
    
    # Standard published PHQ-9 severity categories
    if total <= 4:
        severity = "Minimal or None"
        guidance = "Scores in this range suggest minimal self-reported depressive symptoms. Continuing healthy lifestyle habits, sleep hygiene, and stress management is recommended."
    elif total <= 9:
        severity = "Mild"
        guidance = "Scores in this range suggest mild depressive symptoms. Supportive self-care strategies, regular physical activity, and watchful waiting are often helpful."
    elif total <= 14:
        severity = "Moderate"
        guidance = "Scores in this range suggest moderate symptoms that may be impacting your daily routine. Consulting a healthcare provider or licensed counselor for an evaluation is advisable."
    elif total <= 19:
        severity = "Moderately Severe"
        guidance = "Scores in this range suggest moderately severe symptoms. Professional guidance from a qualified mental health clinician is strongly recommended."
    else:
        severity = "Severe"
        guidance = "Scores in this range suggest severe depressive symptoms significantly interfering with daily functioning. Prompt evaluation by a qualified medical or mental health professional is strongly recommended."
    
    # Critical Safety Trigger: Question 9 (0-indexed index 8)
    # "Thoughts that you would be better off dead or of hurting yourself in some way"
    has_self_harm_ideation = (answers[8] > 0)
    
    return {
        "instrument": "PHQ-9",
        "total_score": total,
        "max_score": 27,
        "severity": severity,
        "guidance": guidance,
        "safety_alert": has_self_harm_ideation,
        "breakdown": [
            {"question": PHQ9_QUESTIONS[i], "score": answers[i]}
            for i in range(9)
        ]
    }

def score_gad7(answers: List[int]) -> Dict[str, Any]:
    """
    Computes GAD-7 score and severity level.
    Score range: 0 to 21.
    """
    if len(answers) != 7:
        raise ValueError(f"GAD-7 requires exactly 7 responses. Received: {len(answers)}")
    
    total = sum(answers)
    
    # Standard published GAD-7 severity categories
    if total <= 4:
        severity = "Minimal Anxiety"
        guidance = "Scores in this range suggest minimal self-reported anxiety symptoms. Everyday stress management, grounding exercises, and regular rest can maintain your wellness."
    elif total <= 9:
        severity = "Mild Anxiety"
        guidance = "Scores in this range suggest mild anxiety symptoms. Mindfulness, paced breathing, and structured time management can be very supportive."
    elif total <= 14:
        severity = "Moderate Anxiety"
        guidance = "Scores in this range suggest moderate anxiety that may affect your comfort or focus. Exploring counseling or speaking with a healthcare professional can provide structured support."
    else:
        severity = "Severe Anxiety"
        guidance = "Scores in this range reflect severe anxiety symptoms that may significantly impair daily activities. Professional evaluation by a mental health professional is strongly encouraged."
        
    return {
        "instrument": "GAD-7",
        "total_score": total,
        "max_score": 21,
        "severity": severity,
        "guidance": guidance,
        "safety_alert": False,
        "breakdown": [
            {"question": GAD7_QUESTIONS[i], "score": answers[i]}
            for i in range(7)
        ]
    }
