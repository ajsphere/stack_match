import streamlit as st


def show_card(value, index, hidden=False):

    if hidden:
        content = "🂠"
    else:
        content = value

    st.markdown(
        f"""
        <div style="
            height:100px;
            width:100px;
            background:#f8f9fa;
            border-radius:18px;
            border:2px solid #cccccc;
            display:flex;
            justify-content:center;
            align-items:center;
            font-size:50px;
            margin:10px auto;
        ">
            {content}
        </div>
        """,
        unsafe_allow_html=True
    )