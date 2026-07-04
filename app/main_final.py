# DramaFlow Studio v4 — FINAL WIRED PRODUCT APP
# This is the real end-to-end runnable product entry point

import streamlit as st

from src.core.product_controller import ProductController


# -----------------------------
# App config
# -----------------------------
st.set_page_config(
    page_title="DramaFlow Studio v4 (Final)",
    layout="wide"
)

st.title("🎬 DramaFlow Studio v4")
st.caption("Final wired AI product (Engine → DTO → UI fully integrated)")


# -----------------------------
# Init controller (SINGLE SOURCE OF TRUTH)
# -----------------------------
@st.cache_resource
def get_controller():
    return ProductController()


controller = get_controller()


# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.header("📌 History")
    for item in controller.get_history():
        st.write(item.get("query", ""))

    st.divider()

    st.header("✨ Recommendations")
    for r in controller.get_recommendations():
        st.write(r)


# -----------------------------
# Input
# -----------------------------
query = st.text_input("Enter your creative prompt")


# -----------------------------
# Main Flow
# -----------------------------
if st.button("Search") and query:

    with st.spinner("Running AI pipeline..."):
        response = controller.search(query)

    # -----------------------------
    # Safety check
    # -----------------------------
    if not response or not response.results:
        st.warning("No results found.")
    else:

        # -----------------------------
        # Intent / summary
        # -----------------------------
        st.subheader("🧠 Understanding")
        st.write(f"Intent: {response.intent}")
        st.write(f"Enhanced Query: {response.enhanced_query}")

        # -----------------------------
        # Results Grid (Product UI)
        # -----------------------------
        st.subheader("🖼 Results")

        cols = st.columns(3)

        for idx, r in enumerate(response.results[:9]):
            with cols[idx % 3]:

                st.markdown("---")

                if r.image_url:
                    st.image(r.image_url, use_container_width=True)

                st.markdown(f"### {r.title}")

                if r.score:
                    st.write(f"Score: {r.score}")

                if r.tags:
                    st.write("Tags:", ", ".join(r.tags))

                if r.explanation:
                    st.info(r.explanation)


# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("✔ Fully wired product version — DramaFlow Studio v4 Final")