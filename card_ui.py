import streamlit as st


def show_card(value, index, hidden=False):

    if hidden:
        content = "🂠"
        background = "#1f4e79"
    else:
        content = value
        background = "#ffffff"


    if hidden:

        clicked = st.button(
            content,
            key=f"card_{index}"
        )

        st.markdown(
            f"""
            <style>
            button[kind="secondary"] {{
                height:120px;
                width:100px;
                border-radius:20px;
                border:2px solid #cccccc;
                background:{background};
                font-size:45px;
                box-shadow:0 4px 8px rgba(0,0,0,0.15);
            }}

            button[kind="secondary"] p {{
                font-size:45px !important;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

        return clicked


    else:

        st.markdown(
            f"""
            <div style="
                height:120px;
                width:100px;
                background:{background};
                border-radius:20px;
                border:2px solid #cccccc;
                display:flex;
                justify-content:center;
                align-items:center;
                font-size:45px;
                margin:10px;
                box-shadow:0 4px 8px rgba(0,0,0,0.15);
            ">
                {content}
            </div>
            """,
            unsafe_allow_html=True
        )

        return False