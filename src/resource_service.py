from typing import List, Dict, Any

RESOURCES_DATA = [
    {
        "id": "grounding-54321",
        "category": "Grounding & Anxiety",
        "title": "5-4-3-2-1 Sensory Grounding Technique",
        "description": "A classic sensory exercise designed to pull you out of anxiety loops and bring your awareness back into the physical present.",
        "steps": [
            "Acknowledge 5 things you see around you right now.",
            "Acknowledge 4 things you can physically touch or feel.",
            "Acknowledge 3 distinct sounds you can hear.",
            "Acknowledge 2 distinct scents you can smell.",
            "Acknowledge 1 pleasant taste or take a gentle sip of cold water."
        ],
        "evidence_basis": "Derived from Cognitive Behavioral Therapy (CBT) and somatic grounding practices.",
        "disclaimer": "This exercise is a self-regulation tool and does not substitute for panic disorder clinical treatment."
    },
    {
        "id": "box-breathing",
        "category": "Breathing & Relaxation",
        "title": "Box Breathing (Square Breathing 4-4-4-4)",
        "description": "Used widely by professionals and athletes to regulate autonomic nervous system arousal during acute stress.",
        "steps": [
            "Exhale all air completely from your lungs.",
            "Inhale slowly through your nose for a count of 4.",
            "Hold your breath gently at the top for a count of 4.",
            "Exhale smoothly through your mouth for a count of 4.",
            "Hold empty at the bottom for a count of 4.",
            "Repeat this cycle for 4 to 6 rounds."
        ],
        "evidence_basis": "Stimulates the vagus nerve and activates the parasympathetic 'rest and digest' response.",
        "disclaimer": "If you experience dizziness, return to natural breathing."
    },
    {
        "id": "cognitive-reframing",
        "category": "Cognitive Strategies",
        "title": "Cognitive Reframing (Thought Checking)",
        "description": "A structured method to identify catastrophic or all-or-nothing thinking and develop balanced, realistic perspectives.",
        "steps": [
            "Write down the stressful thought exactly as it appears in your mind.",
            "Identify any cognitive distortion (e.g., catastrophizing, mind-reading, black-and-white thinking).",
            "Examine the evidence: What real facts support this thought? What facts contradict it?",
            "Formulate an objective, balanced alternative: 'Even if this is difficult, I can handle the next step.'"
        ],
        "evidence_basis": "Core methodology of Cognitive Behavioral Therapy (Beck, 1979).",
        "disclaimer": "Educational exercise for everyday stress management; not individual psychotherapy."
    },
    {
        "id": "sleep-hygiene",
        "category": "Sleep Quality",
        "title": "Evidence-Based Sleep Hygiene Essentials",
        "description": "Habits and environmental modifications that promote consistent circadian rhythm and restful sleep.",
        "steps": [
            "Keep consistent wake and sleep times even on weekends.",
            "Avoid bright phone, tablet, and laptop screens within 45 minutes of bedtime.",
            "Keep the sleeping environment cool (around 18-20°C / 65-68°F), dark, and quiet.",
            "Reserve your bed exclusively for sleep so the brain maintains strong contextual cues.",
            "If you cannot sleep after 20 minutes, get up and do a quiet, dim-light activity until sleepy."
        ],
        "evidence_basis": "Standard sleep medicine recommendations (American Academy of Sleep Medicine).",
        "disclaimer": "For chronic insomnia, consult a sleep specialist or healthcare professional."
    },
    {
        "id": "finding-professional-help",
        "category": "Professional Support",
        "title": "How to Find Qualified Mental Health Support",
        "description": "Guidance on selecting licensed clinical psychologists, psychiatrists, or accredited counseling services.",
        "steps": [
            "Check licensing credentials: Look for M.Phil / Ph.D in Clinical Psychology, RCI licensing (India), or state board certification (US/UK).",
            "Explore tele-mental health options: Official platforms often provide sliding-scale or subsidized counseling sessions.",
            "Prepare for your first session: Write down your key symptoms, how long they have persisted, and any questions about therapy approaches.",
            "Remember that finding the right therapeutic fit is a normal process—it is okay to speak with more than one professional."
        ],
        "evidence_basis": "Guidelines from the World Health Organization (WHO) and American Psychological Association (APA).",
        "disclaimer": "MindCare AI does not endorse specific private practitioners or receive referral compensation."
    }
]

def get_all_resources() -> List[Dict[str, Any]]:
    """Return all verified coping resources."""
    return RESOURCES_DATA

def filter_resources(category: str = "All", search_query: str = "") -> List[Dict[str, Any]]:
    """Filter resources by category and text search query."""
    results = RESOURCES_DATA
    if category != "All":
        results = [r for r in results if r["category"] == category]
    if search_query:
        q = search_query.lower()
        results = [
            r for r in results
            if q in r["title"].lower() or q in r["description"].lower() or any(q in s.lower() for s in r["steps"])
        ]
    return results
