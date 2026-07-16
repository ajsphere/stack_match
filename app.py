import streamlit as st
from cards import cards

st.set_page_config(
    page_title="StackMatch",
    page_icon="🧠"
)

st.title("🧠 StackMatch")

st.write(
    "A memory game for developers. Match programming technologies!"
)

st.info("Game is coming soon 🚀")

columns = st.columns(4)

for index, card in enumerate(cards):
    emoji, name = card

    with columns[index % 4]:
        st.write(emoji)
        st.write(name)