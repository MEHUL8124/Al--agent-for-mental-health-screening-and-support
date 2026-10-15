from typing import Dict, Any

def generate_local_supportive_response(intent: str, user_text: str) -> str:
    """
    Generates structured, empathetic, CBT/grounding-informed supportive responses
    when running locally without an external LLM API key.
    """
    if intent == "grounding":
        return """I hear how intense and overwhelming things feel right now. Let's pause together and ground yourself in the present moment:

🌿 **5-4-3-2-1 Sensory Grounding Technique:**
1. **5 things you can see**: Look around the room and name 5 specific objects (a book, a shadow, a pattern).
2. **4 things you can physically touch**: Feel your feet firmly against the floor, the texture of your clothes, or a cool surface.
3. **3 things you can hear**: Listen closely for background sounds (traffic outside, a hum of a fan, your own breath).
4. **2 things you can smell**: Notice any scent in the air, or take a sip of fresh water.
5. **1 positive sensation**: Place your hand gently on your chest and feel the gentle rise and fall of your breathing.

Take a slow, deep breath in for 4 counts, hold for 4, and release slowly for 6. How is your body feeling right now?"""

    elif intent == "anxiety":
        return """It is completely understandable to feel anxious and tense when facing uncertainties or heavy pressure. Your nervous system is trying to protect you, but we can help it find calm:

🧘 **Box Breathing Practice (4x4):**
- **Inhale** slowly through your nose for **4 seconds**.
- **Hold** that breath gently for **4 seconds**.
- **Exhale** smoothly through your mouth for **4 seconds**.
- **Pause** empty for **4 seconds**.
*(Repeat this cycle 3-4 times)*

💭 **Helpful Reframing Question:**
Is there something in this situation that is within your direct control right now, or is your mind worrying about possibilities beyond this moment? We can break things down together one small step at a time."""

    elif intent == "depression_sadness":
        return """Thank you for sharing this with me. When sadness or emptiness settles in, even everyday tasks can feel like moving through heavy water.

Please remember:
- **Be gentle with yourself**: You don't have to fix everything today. Resting and acknowledging your feelings without self-judgment is valid.
- **The 'Micro-Step' Rule**: If getting things done feels impossible, pick the smallest possible action: drinking one glass of water, opening a window for fresh air, or sitting comfortably for 5 minutes.
- **Human Connection**: Sharing your burden with a trusted friend, family member, or counselor often lightens the weight. Would you like to explore some gentle reflection prompts or coping resources?"""

    elif intent == "sleep_trouble":
        return """Restless nights can make everything in daytime feel twice as difficult. Here are evidence-informed tips for restorative sleep:

🌙 **Wind-down Routine:**
1. **Screen Dimming**: Blue light delays melatonin release; consider switching to a warm lamp or listening to gentle audio.
2. **Brain Dump**: Write down tomorrow's to-do list on paper so your mind doesn't have to carry the fear of forgetting.
3. **4-7-8 Relaxing Breath**: Inhale for 4 seconds, hold for 7, exhale slowly with a whoosh sound for 8 seconds. This naturally stimulates your parasympathetic nervous system."""

    elif intent == "coping_resources":
        return """Here are some practical tools you can explore right now:
- **Guided Exercises**: Visit the **Coping Strategies & Resources** tab in the sidebar for full guides on Progressive Muscle Relaxation, Box Breathing, and Sleep Hygiene.
- **Reflection Journaling**: Write freely without editing—letting your thoughts flow onto paper helps externalize stress.
- **Professional Guidance**: When distress persists, speaking with a licensed therapist or mental health counselor provides personalized, compassionate care."""

    elif intent == "gratitude_progress":
        return """It is wonderful to hear that! Taking a moment to notice and celebrate positive shifts—no matter how small—is a powerful foundation for emotional resilience. What contributed to this feeling today?"""

    else:
        return """Thank you for opening up and sharing. I'm here as a supportive, reflective space.

While I am an AI wellness companion and cannot offer clinical diagnoses or therapy, I am always here to listen, offer grounding exercises, or explore coping strategies.

Would you like to try a short breathing exercise, write down what's on your mind, or explore practical strategies to navigate your day?"""
