import streamlit as st


def hero(
    title: str,
    subtitle: str,
    description: str,
):

    st.markdown(

        f"""

<div class="hero">

<h1>{title}</h1>

<h2>{subtitle}</h2>

<p>{description}</p>

</div>

""",

        unsafe_allow_html=True,

    )