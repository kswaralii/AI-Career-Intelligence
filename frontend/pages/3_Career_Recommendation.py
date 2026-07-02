import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Career Recommendation",
    page_icon="💼",
    layout="wide"
)

st.title("💼 Career Recommendation")
st.caption("Discover roles that align with your current skill profile.")

if not st.session_state.get("resume_uploaded", False):
    st.warning("Upload your resume from the Home page first.")
    st.stop()

st.success(
    f"Active resume: {st.session_state.get('resume_filename', 'Resume.pdf')}"
)

recommend = st.button(
    "Find Career Matches",
    use_container_width=True
)

if recommend:

    with st.spinner("Finding suitable career roles..."):

        response = requests.post(
            f"{API_URL}/career/recommend",
            json={
                "resume_id": st.session_state["resume_id"]
            }
        )

    if response.status_code == 200:

        st.session_state["career_result"] = response.json()

    else:

        st.error("Career recommendation failed.")
        st.code(response.text)

if "career_result" in st.session_state:

    result = st.session_state["career_result"]

    roles = result.get("recommended_roles", [])

    st.divider()
    st.subheader("Top Career Matches")

    if not roles:

        st.info("No career matches found.")

    else:

        medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"]

        for i, role in enumerate(roles[:5]):

            role_name = role.get("role", "Career Role")
            match_score = role.get("match_percentage", 0)

            col1, col2 = st.columns([4, 1])

            with col1:
                st.markdown(
                    f"### {medals[i]} {role_name}"
                )

            with col2:
                st.metric(
                    "Match",
                    f"{match_score}%"
                )

            st.progress(match_score / 100)

            if i < len(roles[:5]) - 1:
                st.divider()