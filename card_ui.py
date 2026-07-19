import streamlit as st


def show_card(value, index, hidden=False):

    st.markdown(
        """
        <style>

        div[data-testid="stButton"]:has(button[kind="secondary"]) button {
            height: 130px;
            width: 130px;
            border-radius: 25px;
            font-size: 70px;
            background-color: #ffe5ec;
            border: 3px solid #ff8fab;
        }

        div[data-testid="stButton"]:has(button[kind="secondary"]) button p {
            font-size: 70px !important;
        }

        </style>
        """,
        unsafe_allow_html=True
    )


    if hidden:

        clicked = st.button(
            "🍬",
            key=f"card_{index}",
            use_container_width=True
        )

        return clicked


    else:

        st.button(
            value,
            key=f"open_{index}",
            disabled=True,
            use_container_width=True
        )

        return False