import streamlit as st


def resume_status(filename: str):

    st.markdown(

        f"""

<div class="status-card">

<h3>Resume Uploaded Successfully</h3>

<p>

<strong>File:</strong> {filename}

<br><br>

Your resume has been processed successfully and is now available
for ATS Analysis, Career Recommendation and AI Career Coach.

</p>

</div>

""",

        unsafe_allow_html=True,

    )