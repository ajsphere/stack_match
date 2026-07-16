import streamlit as st
from cards import cards

st.set_page_config(
    page_title="StackMatch",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 StackMatch")

st.write("A memory game for developers.")

st.info("🚀 Version 1.0")

columns = st.columns(4)

for index, card in enumerate(cards):

    with columns[index % 4]:
        st.write(card["value"])