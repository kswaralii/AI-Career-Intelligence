import requests
import streamlit as st

from utils.config import BACKEND_URL
from utils.pdf_generator import create_report

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🤖",
    layout="wide"
)

st.title("CareerPilot AI")
st.caption("AI-powered career intelligence for placement preparation")

st.write(
    "Analyze resume-job alignment, identify skill gaps, explore suitable roles, "
    "and receive targeted career guidance."
)

st.divider()

has_resume = st.session_state.get("resume_uploaded", False)
has_ats = "ats_result" in st.session_state
has_career = "career_result" in st.session_state
has_coach = "coach_result" in st.session_state

st.subheader("Career Readiness Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Resume Profile",
        "Processed" if has_resume else "Pending"
    )

with col2:
    st.metric(
        "ATS Evaluation",
        "Completed" if has_ats else "Pending"
    )

with col3:
    st.metric(
        "Career Fit",
        "Completed" if has_career else "Pending"
    )

with col4:
    st.metric(
        "AI Guidance",
        "Generated" if has_coach else "Optional"
    )

st.divider()

left_col, right_col = st.columns([1.4, 1])

with left_col:

    st.subheader("Resume Profile Setup")

    st.write(
        "Upload your resume in PDF format to create a personalized "
        "career intelligence profile."
    )

    uploaded_file = st.file_uploader(
        "Select Resume (PDF)",
        type=["pdf"]
    )

    if uploaded_file is not None:

        st.caption(f"Selected document: {uploaded_file.name}")

        if st.button(
            "Process Resume",
            use_container_width=True
        ):

            with st.spinner(
                "Processing resume and extracting relevant skills..."
            ):

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

                st.session_state.pop("ats_result", None)
                st.session_state.pop("career_result", None)
                st.session_state.pop("coach_result", None)

                st.success(
                    "Resume processed successfully. Your career profile is ready."
                )

                st.rerun()

            else:

                st.error("Unable to process the resume.")
                st.code(response.text)

with right_col:

    st.subheader("Platform Capabilities")

    st.markdown(
        """
        Assess alignment between your resume and a target job description.

        Identify roles that align with your current skill profile.

        Understand which skills require focused development.
       
        Receive targeted project, roadmap, and interview recommendations.
 
        Download a consolidated PDF report of completed analyses.
        """
    )

st.divider()

if st.session_state.get("resume_uploaded"):

    st.subheader("Career Intelligence Workspace")

    workspace_col1, workspace_col2 = st.columns([1.4, 1])

    with workspace_col1:

        st.success("Resume uploaded successfully")

        st.markdown(
            f"""
            **Active Resume**  
            `{st.session_state.get("resume_filename", "Resume.pdf")}`
            """
        )

        completed = sum([has_ats, has_career, has_coach])

        st.progress(completed / 3)

        st.caption(
            f"{completed} of 3 career intelligence modules completed. "
            "AI Career Guidance is optional."
        )

    with workspace_col2:

        st.markdown("#### Career Intelligence Report")

        if has_ats or has_career or has_coach:

            st.caption(
                "The report includes all analyses completed for the active resume."
            )

            pdf_file = create_report(
                filename=st.session_state.get(
                    "resume_filename",
                    "Resume.pdf"
                ),
                ats_result=st.session_state.get(
                    "ats_result",
                    None
                ),
                career_result=st.session_state.get(
                    "career_result",
                    None
                ),
                coach_result=st.session_state.get(
                    "coach_result",
                    None
                ),
            )

            with open(pdf_file, "rb") as file:

                st.download_button(
                    label="Download Career Intelligence Report",
                    data=file,
                    file_name="CareerPilot_Report.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                )

        else:

            st.info(
                "Complete ATS Resume Evaluation or Career Role Recommendation "
                "to generate your report."
            )

    st.divider()

    st.subheader("Recommended Action")

    if not has_ats:

        st.info(
            "Begin with ATS Resume Evaluation to assess your resume against "
            "a target job description and identify relevant skill gaps."
        )

    elif not has_career:

        st.info(
            "Proceed to Career Role Recommendation to identify suitable "
            "career paths based on your extracted skill profile."
        )

    elif not has_coach:

        st.info(
            "Optional: Use AI Career Guidance for personalized project ideas, "
            "learning roadmaps, and interview preparation."
        )

    else:

        st.success(
            "Your career intelligence profile is complete. "
            "You can download the consolidated report above."
        )