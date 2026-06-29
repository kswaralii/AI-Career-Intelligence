import streamlit as st
import requests

from utils.config import BACKEND_URL

st.set_page_config(
    page_title="AI Career Intelligence Platform",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Career Intelligence Platform")

st.write(
    """
Welcome to the AI Career Intelligence Platform.

Upload your resume once and use all the features from the sidebar.
"""
)

st.divider()

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file is not None:

    if st.button("Upload Resume", use_container_width=True):

        with st.spinner("Uploading Resume..."):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    "application/pdf"
                )
            }

            response = requests.post(
                f"{BACKEND_URL}/resume/upload",
                files=files
            )

        if response.status_code == 200:

            data = response.json()

            st.session_state["resume_uploaded"] = True
            st.session_state["resume_filename"] = uploaded_file.name
            st.session_state["resume_id"] = data["resume_id"]

            st.success("✅ Resume uploaded successfully!")

        else:

            st.error(f"Status Code: {response.status_code}")
            st.write(response.text)

if st.session_state.get("resume_uploaded"):

    st.divider()

    st.success("✅ Resume Ready")

    st.write(
        f"**Uploaded Resume:** {st.session_state['resume_filename']}"
    )

    st.info(
        """
Your resume has been processed successfully.

You can now use:

• 🎯 Resume Analysis

• 💼 Career Recommendation

• 💰 Salary Prediction

• 🤖 AI Career Coach
"""
    )