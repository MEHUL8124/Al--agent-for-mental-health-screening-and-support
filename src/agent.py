import os
from typing import List, Dict, Any, Tuple
from src import config, safety, intent_classifier, response_engine, resource_service

SYSTEM_PROMPT = """You are MindCare AI, an empathetic, supportive mental wellness companion.
Guidelines you must strictly follow:
1. Speak in a warm, calm, compassionate, and non-judgmental tone.
2. IMPORTANT: You are NOT a doctor, therapist, or diagnostic medical system. NEVER diagnose any mental health condition (such as clinical depression or generalized anxiety disorder).
3. Do NOT recommend prescription medications or alter treatments.
4. Offer evidence-informed, general self-care coping techniques such as sensory grounding (5-4-3-2-1), paced breathing, cognitive reframing prompts, or breaking challenges into small steps.
5. If the user mentions persistent suffering, gently encourage seeking a qualified licensed healthcare or mental health professional.
6. Keep responses clear, helpful, and accessible without being overly lengthy.
"""

def generate_agent_response(
    user_message: str,
    chat_history: List[Dict[str, str]],
    region: str = "India"
) -> Dict[str, Any]:
    """
    Primary agent pipeline:
    1. Safety & crisis detection (high priority override)
    2. Intent classification
    3. LLM generation if API key is present
    4. Deterministic CBT-informed fallback if no API key or upon failure
    """
    # Step 1: Safety & Crisis Detection
    is_crisis, crisis_reason = safety.check_crisis_indicators(user_message)
    if is_crisis:
        crisis_data = safety.get_crisis_response(region)
        return {
            "response": crisis_data["message"],
            "intent": "crisis",
            "is_crisis": True,
            "mode": "safety_override",
            "resources": crisis_data["helplines"]
        }
        
    # Step 2: Intent Classification
    intent_data = intent_classifier.classify_intent(user_message)
    detected_intent = intent_data["intent"]
    
    # Step 3: Check for LLM API configuration
    api_key = config.OPENAI_API_KEY
    if api_key:
        try:
            import openai
            client = openai.OpenAI(api_key=api_key)
            
            # Format message history (last 6 turns for context management)
            messages = [{"role": "system", "content": SYSTEM_PROMPT}]
            for turn in chat_history[-6:]:
                messages.append({"role": turn["role"], "content": turn["content"]})
            messages.append({"role": "user", "content": user_message})
            
            completion = client.chat.completions.create(
                model=config.OPENAI_MODEL,
                messages=messages,
                temperature=0.7,
                max_tokens=600
            )
            llm_text = completion.choices[0].message.content
            return {
                "response": llm_text,
                "intent": detected_intent,
                "is_crisis": False,
                "mode": "generative_llm",
                "resources": []
            }
        except Exception as e:
            # Fallback gracefully upon any API error or quota limit
            fallback_text = response_engine.generate_local_supportive_response(detected_intent, user_message)
            return {
                "response": f"{fallback_text}\n\n*(Note: LLM provider unavailable ({type(e).__name__}); responded via built-in supportive engine)*",
                "intent": detected_intent,
                "is_crisis": False,
                "mode": "offline_support_fallback",
                "resources": []
            }
            
    # Step 4: Transparent Rule-based Offline Support Engine
    offline_text = response_engine.generate_local_supportive_response(detected_intent, user_message)
    return {
        "response": offline_text,
        "intent": detected_intent,
        "is_crisis": False,
        "mode": "offline_support",
        "resources": []
    }
