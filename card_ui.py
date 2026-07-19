import streamlit as st


def show_card(value, index, hidden=False):

    st.markdown(
        """
        <style>

        div[data-testid="stButton"] button {
            height: 130px;
            width: 130px;
            border-radius: 25px;
            font-size: 70px;
            border: 3px solid #ff8fab;
            background-color: #ffe5ec;
            transition: 0.3s;
        }


        div[data-testid="stButton"] button:hover {
            transform: scale(1.05);
        }


        div[data-testid="stButton"] button p {
            font-size: 70px !important;
            line-height: 1 !important;
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