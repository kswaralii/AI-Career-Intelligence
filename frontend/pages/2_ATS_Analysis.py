import requests
import streamlit as st

from utils.config import BACKEND_URL

API_URL = BACKEND_URL


def show_skills(skills):

    for skill in skills:
        st.write(f"- {skill}")


st.set_page_config(
    page_title="ATS Analysis",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 ATS Resume Analysis")
st.caption("Compare your resume with a job description.")

if not st.session_state.get("resume_uploaded", False):
    st.warning("Upload your resume from the Home page first.")
    st.stop()

st.success(
    f"Active resume: {st.session_state.get('resume_filename', 'Resume.pdf')}"
)

job_description = st.text_area(
    "Paste Job Description",
    height=230,
    placeholder="Paste the complete job description here..."
)

analyze = st.button(
    "Analyze Resume",
    use_container_width=True
)

if analyze:

    if len(job_description.split()) < 30:
        st.warning("Paste a complete job description (at least 30 words).")
        st.stop()

    with st.spinner("Analyzing..."):

        response = requests.post(
            f"{API_URL}/ats/analyze",
            json={
                "resume_id": st.session_state["resume_id"],
                "job_description": job_description
            }
        )

    if response.status_code == 200:
        st.session_state["ats_result"] = response.json()

    else:
        st.error("ATS analysis failed.")
        st.code(response.text)

if "ats_result" in st.session_state:

    result = st.session_state["ats_result"]

    score = result.get("ats_score", 0)
    matched = result.get("matched_skills", [])
    missing = result.get("missing_skills", [])
    recommendations = result.get("recommendations", [])

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Skill Match Score", f"{score}%")

    with col2:
        st.metric("Matched Skills", len(matched))

    with col3:
        st.metric("Missing Skills", len(missing))

    st.progress(score / 100)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("✅ Matched Skills")

        if matched:

            show_skills(matched[:5])

            if len(matched) > 5:

                with st.expander(
                    f"View all {len(matched)} matched skills"
                ):
                    show_skills(matched)

        else:
            st.info("No matched skills found.")

    with col2:

        st.subheader("⚠️ Skills to Improve")

        if missing:

            show_skills(missing[:5])

            if len(missing) > 5:

                with st.expander(
                    f"View all {len(missing)} missing skills"
                ):
                    show_skills(missing)

        else:
            st.success("No missing skills found.")

    if recommendations:

        st.divider()

        st.subheader("📚 Learning Resources")

        for resource in recommendations[:5]:

            skill = resource.get("skill", "Skill")
            resource_name = resource.get(
                "resource",
                "Learning resource"
            )
            platform = resource.get("platform", "")
            url = resource.get("url", "")

            with st.expander(skill):

                st.write(f"**{resource_name}**")

                if platform:
                    st.caption(platform)

                if url:
                    st.link_button(
                        "Open Resource",
                        url,
                        use_container_width=True
                    )

        if len(recommendations) > 5:

            with st.expander(
                f"View {len(recommendations) - 5} more learning resources"
            ):

                for resource in recommendations[5:]:

                    skill = resource.get("skill", "Skill")
                    resource_name = resource.get(
                        "resource",
                        "Learning resource"
                    )
                    platform = resource.get("platform", "")
                    url = resource.get("url", "")

                    st.write(f"**{skill}** — {resource_name}")

                    if platform:
                        st.caption(platform)

                    if url:
                        st.link_button(
                            f"Open {skill} Resource",
                            url,
                            use_container_width=True
                        )

    elif missing:

        st.info(
            "Learning resources are available only for selected skills."
        )