# 🎨 Streamlit UI (Polish + AI Enhanced Frontend)

import streamlit as st
from src.application.application_service_stable import ApplicationService

service = ApplicationService()

st.set_page_config(
    page_title="DramaFlow Studio v4",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 DramaFlow Studio v4")
st.caption("Internal AI Orchestration Platform")

if "history" not in st.session_state:
    st.session_state.history = []

query = st.text_input("Enter your query")

if st.button("Run") and query:
    result = service.execute_query(query)
    st.session_state.history.append((query, result))

    st.subheader("📌 Result")
    st.write("Enhanced Query:", result.enhanced_query)
    st.write("Intent:", result.intent)

    st.subheader("📊 Output")
    st.json({"results": result.results})

st.divider()

st.subheader("🕘 History")
for q, r in reversed(st.session_state.history[-10:]):
    st.markdown(f"**Q:** {q}")
    st.markdown(f"**Intent:** {r.intent}")
    st.markdown("---")