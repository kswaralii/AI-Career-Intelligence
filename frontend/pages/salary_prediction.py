import streamlit as st

if not st.session_state.get("resume_uploaded"):

    st.warning("⚠️ Please upload your resume from the Home page first.")

    st.stop()

st.title("💰 Salary Prediction")