import streamlit as st


def show_card(value, index):

    st.markdown(
        f"""
        <div style="
            height:90px;
            width:90px;
            background:#ffffff;
            border-radius:15px;
            border:2px solid #dddddd;
            display:flex;
            justify-content:center;
            align-items:center;
            font-size:45px;
            margin:10px;
        ">
            {value}
        </div>
        """,
        unsafe_allow_html=True
    )