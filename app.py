import random
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

game_cards = cards.copy()
random.shuffle(game_cards)

if "flipped_cards" not in st.session_state:
    st.session_state.flipped_cards = []

columns = st.columns(4)

for index, card in enumerate(game_cards):

    with columns[index % 4]:
        st.write(card["value"])