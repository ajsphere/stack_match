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
                height: 120px;
                width: 120px;
                border-radius: 20px;
                background-color: #c7f9cc;
                border: 3px solid #57cc99;
            }


            div[data-testid="stButton"] button p {
                font-size: 70px !important;
                line-height: 1 !important;
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
                height: 120px;
                width: 120px;
                border-radius: 20px;
                background-color: #ffd6a5;
                border: 3px solid #ff9f1c;
            }


            div[data-testid="stButton"] button p {
                font-size: 70px !important;
                line-height: 1 !important;
            }


            </style>
            """,
            unsafe_allow_html=True
        )


        return False