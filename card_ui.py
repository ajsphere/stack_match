import streamlit as st


def show_card(value, index, hidden=False):

    if hidden:

        clicked = st.button(
            "🍭",
            key=f"card_{index}",
            use_container_width=True
        )

        st.markdown(
            """
            <style>
            div[data-testid="stButton"] button {
                height: 90px;
                font-size: 35px;
                border-radius: 15px;
                background-color: #ffd6e7;
                border: 3px solid #ff8fab;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        return clicked


    else:

        st.button(
            value,
            key=f"open_{index}",
            disabled=True,
            use_container_width=True
        )

        st.markdown(
            """
            <style>
            div[data-testid="stButton"] button {
                height: 90px;
                font-size: 35px;
                border-radius: 15px;
                background-color: #fff0f5;
                border: 3px solid #ff8fab;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        return False