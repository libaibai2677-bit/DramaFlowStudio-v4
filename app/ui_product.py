# DramaFlow Studio v4 — Product-Level UI (Polished Streamlit App)
# Safe version: separate file to avoid overwrite conflicts

import streamlit as st

from src.services.history_service import HistoryService
from src.services.recommendation_service import RecommendationService
from src.services.explainability_service import ExplainabilityService
from src.core.unified_engine import UnifiedEngine


st.set_page_config(
    page_title="DramaFlow Studio v4",
    layout="wide"
)

st.title("🎬 DramaFlow Studio — Product UI v2")
st.caption("Polished runnable AI product interface")


@st.cache_resource
def init_system():
    history = HistoryService()
    recommendation = RecommendationService(history)
    explain = ExplainabilityService()
    engine = UnifiedEngine()
    return history, recommendation, explain, engine


history_service, recommendation_service, explain_service, engine = init_system()


# Sidebar
with st.sidebar:
    st.header("History")
    for item in history_service.last(10):
        st.write(item.get("query"))

    st.header("Recommendations")
    for r in recommendation_service.get_recommendations():
        st.write(r)


query = st.text_input("Enter prompt")

if st.button("Run") and query:

    with st.spinner("Processing AI pipeline..."):
        result = engine.search(query)

    enhanced_query = result.get("enhanced_query", query)
    intent = result.get("intent", "default")
    results = result.get("results", [])

    explained = explain_service.explain_results(
        query, enhanced_query, intent, results
    )

    history_service.add(query, enhanced_query, intent, results)

    st.subheader("Results")
    st.write(explained)

    st.subheader("Intent")
    st.write(intent)

    st.subheader("Explanation")
    st.write(explain_service.explain_summary(intent))