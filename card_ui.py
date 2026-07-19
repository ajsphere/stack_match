import streamlit as st


def show_card(value, index, hidden=False):

    if hidden:
        content = "🂠"
        background = "#1f4e79"
    else:
        content = value
        background = "#ffffff"


    st.markdown(
        f"""
        <style>
        div[data-testid="stButton"] button {{
            height:120px;
            width:100px;
            background:{background};
            border-radius:20px;
            border:2px solid #cccccc;
            font-size:45px;
            margin:10px;
            box-shadow:0 4px 8px rgba(0,0,0,0.15);
        }}

        div[data-testid="stButton"] button p {{
            font-size:45px !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


    if hidden:

        clicked = st.button(
            content,
            key=f"card_{index}",
            use_container_width=False
        )

        return clicked


    else:

        st.button(
            content,
            key=f"open_{index}",
            disabled=True,
            use_container_width=False
        )

        return False