import streamlit as st


def feature_card(
    title: str,
    description: str,
    features: list[str],
):

    items = ""

    for feature in features:

        items += f"<li>{feature}</li>"

    st.markdown(

        f"""

<div class="card">

<h3>{title}</h3>

<p>{description}</p>

<ul>

{items}

</ul>

</div>

""",

        unsafe_allow_html=True,

    )