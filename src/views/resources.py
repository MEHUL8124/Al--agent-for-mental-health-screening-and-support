import streamlit as st
from src import resource_service, config

def render():
    st.title("🌿 Coping Strategies & Mental Health Resources")
    st.caption("Evidence-informed self-regulation practices, grounding techniques, and verified helplines.")
    
    col_search, col_cat = st.columns([2, 1])
    with col_search:
        search_query = st.text_input("🔍 Search techniques or keywords:", placeholder="e.g. breathing, sleep, grounding, panic...")
    with col_cat:
        category = st.selectbox(
            "Category Filter:",
            ["All", "Grounding & Anxiety", "Breathing & Relaxation", "Cognitive Strategies", "Sleep Quality", "Professional Support"]
        )
        
    filtered = resource_service.filter_resources(category=category, search_query=search_query)
    
    st.markdown("---")
    
    if not filtered:
        st.info("No matching coping resources found for your query. Try searching for 'breathing' or 'grounding'.")
    else:
        for res in filtered:
            with st.container():
                st.markdown(f"### {res['title']}")
                st.caption(f"Category: **{res['category']}** | Evidence: *{res['evidence_basis']}*")
                st.write(res["description"])
                
                with st.expander("👉 View Practical Step-by-Step Exercise"):
                    for step in res["steps"]:
                        st.markdown(f"- {step}")
                    st.caption(f"⚠️ *{res['disclaimer']}*")
                st.markdown("<hr style='margin: 1.2rem 0; opacity: 0.2;'>", unsafe_allow_html=True)
                
    st.markdown("---")
    st.subheader("🚨 24/7 Verified Emergency & Crisis Contacts")
    region = st.session_state.get("selected_region", config.DEFAULT_REGION)
    info = config.CRISIS_RESOURCES.get(region, config.CRISIS_RESOURCES["India"])
    
    st.error(f"**Immediate Life Safety / Emergency**: Call **{info['emergency']}**")
    st.markdown(f"**Free, confidential 24/7 crisis hotlines for {region}:**")
    for h in info["helplines"]:
        st.write(f"- **{h['name']}** ({h['type']}): `{h['contact']}` — {h['details']}")
