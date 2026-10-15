import streamlit as st
from src import agent, config

def render():
    st.title("💬 AI Support Chat")
    st.caption("Empathetic, reflective conversations and evidence-informed coping techniques.")
    
    st.info("🔒 **Privacy Notice**: Messages are processed strictly for this active session. No conversation history is uploaded to an external database. Remember: MindCare AI is a wellness assistant, not a therapist or emergency service.")
    
    # Initialize session state for chat
    if "chat_messages" not in st.session_state:
        st.session_state["chat_messages"] = [
            {
                "role": "assistant",
                "content": "Hello. I'm MindCare AI, your supportive wellness companion. Whether you'd like to talk through stress, practice a grounding exercise, or explore coping tools, I'm here to listen. How are you feeling today?"
            }
        ]
        
    # Quick Starter Prompts
    st.write("**Quick conversation starters:**")
    prompt_cols = st.columns(3)
    with prompt_cols[0]:
        if st.button("🌿 Guide me through a 5-4-3-2-1 grounding exercise", key="quick_grounding"):
            handle_message("I am feeling really anxious and overwhelmed right now. Please guide me through a 5-4-3-2-1 sensory grounding exercise.")
    with prompt_cols[1]:
        if st.button("🧘 Help me calm down with paced breathing", key="quick_breathing"):
            handle_message("My heart is beating fast and I feel stressed. Can we do a box breathing exercise together?")
    with prompt_cols[2]:
        if st.button("🌙 Tips for sleeping when my mind is racing", key="quick_sleep"):
            handle_message("I am having a lot of trouble sleeping tonight because my thoughts won't stop racing.")

    st.markdown("---")
    
    # Display message history
    for msg in st.session_state["chat_messages"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            
    # Chat Input Box
    user_input = st.chat_input("Type your message here... (e.g., 'I feel overwhelmed with work today')")
    if user_input:
        handle_message(user_input)

    st.markdown("---")
    col_clear, col_mode = st.columns([1, 2])
    with col_clear:
        if st.button("🗑️ Clear Chat History"):
            st.session_state["chat_messages"] = [
                {
                    "role": "assistant",
                    "content": "Chat history cleared. I'm ready whenever you'd like to talk."
                }
            ]
            st.rerun()
            
    with col_mode:
        if config.OPENAI_API_KEY:
            st.caption("🟢 Mode: Generative AI Connected (OpenAI API)")
        else:
            st.caption("🛡️ Mode: Built-in Offline Supportive Response Engine (Deterministic & Private)")

def handle_message(text: str):
    # Add user message
    st.session_state["chat_messages"].append({"role": "user", "content": text})
    
    # Generate agent response
    region = st.session_state.get("selected_region", config.DEFAULT_REGION)
    agent_output = agent.generate_agent_response(
        user_message=text,
        chat_history=st.session_state["chat_messages"],
        region=region
    )
    
    # Add assistant response
    st.session_state["chat_messages"].append({
        "role": "assistant",
        "content": agent_output["response"]
    })
    st.rerun()
