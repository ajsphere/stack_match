import streamlit as st


def show_card(value, index, hidden=False):

    st.markdown(
        """
        <style>
        
        .card-button button {
            height: 130px !important;
            width: 130px !important;
            border-radius: 25px !important;
            background-color: #ffe5ec !important;
            border: 3px solid #ff8fab !important;
            font-size: 65px !important;
            padding: 0 !important;
        }

        .card-button button p {
            font-size: 65px !important;
            line-height: 1 !important;
        }

        </style>
        """,
        unsafe_allow_html=True
    )


    if hidden:

        with st.container():

            clicked = st.button(
                "🍬",
                key=f"card_{index}",
                use_container_width=True
            )

        return clicked


    else:

        with st.container():

            st.button(
                value,
                key=f"open_{index}",
                disabled=True,
                use_container_width=True
            )

        return False