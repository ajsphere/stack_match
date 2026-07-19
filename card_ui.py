import streamlit as st


def show_card(value, index, hidden=False):

    if hidden:

        clicked = st.button(
            "🍭",
            key=f"card_{index}"
        )

        return clicked


    else:

        st.markdown(
            f"""
            <div style="
                height:90px;
                width:90px;
                display:flex;
                justify-content:center;
                align-items:center;
                background-color:#fff0f5;
                border:3px solid #ff8fab;
                border-radius:15px;
                font-size:35px;
                margin:auto;
            ">
                {value}
            </div>
            """,
            unsafe_allow_html=True
        )

        return False