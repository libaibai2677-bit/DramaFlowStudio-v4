# DramaFlow Studio v4 — Runnable Software (Streamlit MVP)
# This is the first runnable product version: UI + AI pipeline integration point

import streamlit as st
from typing import List, Dict, Any

# Core services
from src.services.history_service import HistoryService
from src.services.recommendation_service import RecommendationService
from src.services.explainability_service import ExplainabilityService

# NOTE:
# UnifiedEngine should already exist in your project.
# If path differs, adjust import accordingly.
from src.core.unified_engine import UnifiedEngine


# -----------------------------
# Initialize system (singleton)
# -----------------------------
@st.cache_resource
def init_system():
    history_service = HistoryService()
    recommendation_service = RecommendationService(history_service)
    explain_service = ExplainabilityService()
    engine = UnifiedEngine()

    return {
        "history": history_service,
        "recommendation": recommendation_service,
        "explain": explain_service,
        "engine": engine
    }


system = init_system()


# -----------------------------
# UI Layout
# -----------------------------
st.set_page_config(page_title="DramaFlow Studio v4", layout="wide")

st.title("🎬 DramaFlow Studio v4")
st.caption("AI-powered Image Search with Explainable Intelligence")

query = st.text_input("Enter your creative prompt:")

if st.button("Search") and query:
    
    # 1. AI Core Processing
    engine = system["engine"]
    result = engine.search(query)

    enhanced_query = result.get("enhanced_query", query)
    intent = result.get("intent", "default")
    results = result.get("results", [])

    # 2. Explainability
    explain_service = system["explain"]
    explained_results = explain_service.explain_results(
        query, enhanced_query, intent, results
    )

    # 3. History
    system["history"].add(query, enhanced_query, intent, results)

    # 4. Recommendations
    recommendations = system["recommendation"].get_recommendations()

    # -----------------------------
    # Display Results
    # -----------------------------
    st.subheader("🖼 Results")

    for item in explained_results[:8]:
        with st.container():
            st.write(item)

    # -----------------------------
    # Explain Panel
    # -----------------------------
    st.subheader("🧠 Explainability")
    st.write(f"Intent: {intent}")
    st.write(explain_service.explain_summary(intent))

    # -----------------------------
    # Recommendations
    # -----------------------------
    st.subheader("✨ Recommendations")
    st.write(recommendations)

    # -----------------------------
    # History
    # -----------------------------
    st.subheader("📌 History")
    st.write(system["history"].last(10))


# Footer
st.markdown("---")
st.caption("Runnable MVP version of DramaFlow Studio v4")