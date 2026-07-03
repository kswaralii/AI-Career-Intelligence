import requests
import streamlit as st

from utils.config import BACKEND_URL

API_URL = BACKEND_URL

st.set_page_config(
    page_title="AI Career Coach",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Career Coach")

if not st.session_state.get("resume_uploaded", False):
    st.warning("Upload your resume from the Home page first.")
    st.stop()

st.success(
    f"Active resume: {st.session_state.get('resume_filename', 'Resume.pdf')}"
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    if st.button("📄 Analyze My Resume", use_container_width=True):
        st.session_state["coach_question"] = "Analyze my resume and identify top improvements."

    if st.button("🚀 Suggest Projects", use_container_width=True):
        st.session_state["coach_question"] = "Suggest three portfolio projects based on my skills."

    if st.button("📚 Learning Roadmap", use_container_width=True):
        st.session_state["coach_question"] = "Create a 30-day learning roadmap based on my resume."

with col2:
    if st.button("💼 Suitable Career Role", use_container_width=True):
        st.session_state["coach_question"] = "Which career role suits my current profile?"

    if st.button("🎯 Improve My Resume", use_container_width=True):
        st.session_state["coach_question"] = "How can I improve my resume for campus placements?"

    if st.button("🎤 Interview Preparation", use_container_width=True):
        st.session_state["coach_question"] = "Give me interview questions based on my resume."

st.divider()

question = st.text_area(
    "Your Career Question",
    value=st.session_state.get("coach_question", ""),
    height=130
)

if st.button("Generate Guidance", use_container_width=True):

    if not question.strip():
        st.warning("Enter a career-related question first.")
        st.stop()

    with st.spinner("Generating guidance..."):

        response = requests.post(
            f"{API_URL}/ai-coach/chat",
            json={
                "resume_id": st.session_state["resume_id"],
                "question": question
            }
        )

    if response.status_code == 200:

        result = response.json()

        st.session_state["coach_result"] = result

        st.divider()
        st.subheader("AI Career Guidance")
        st.markdown(result.get("advice", "No guidance generated."))

    else:
        st.error("AI Career Coach failed.")
        st.code(response.text)