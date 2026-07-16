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
        <div style="
            height:100px;
            width:100px;
            background:{background};
            border-radius:20px;
            border:2px solid #cccccc;
            display:flex;
            justify-content:center;
            align-items:center;
            font-size:50px;
            margin:10px auto;
            box-shadow:0px 4px 10px rgba(0,0,0,0.15);
        ">
            {content}
        </div>
        """,
        unsafe_allow_html=True
    )