import random
import time
import streamlit as st

st.set_page_config(
    page_title="StackMatch",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 StackMatch")

st.write("A memory game for developers.")

st.info("🚀 Version 1.0")

if "game_cards" not in st.session_state:
    st.session_state.game_cards = cards.copy()
    random.shuffle(st.session_state.game_cards)

game_cards = st.session_state.game_cards

if "flipped_cards" not in st.session_state:
    st.session_state.flipped_cards = []

if "matched_cards" not in st.session_state:
    st.session_state.matched_cards = []

columns = st.columns(4)

for index, card in enumerate(game_cards):

    with columns[index % 4]:

        if index in st.session_state.matched_cards:

            st.button(
                card["value"],
                key=index
            )

        elif index in st.session_state.flipped_cards:

            st.button(
                card["value"],
                key=index
            )

        else:

            if st.button("🂠", key=index):
                st.session_state.flipped_cards.append(index)


if len(st.session_state.flipped_cards) == 2:

    first = st.session_state.flipped_cards[0]
    second = st.session_state.flipped_cards[1]

    if game_cards[first]["pair"] == game_cards[second]["pair"]:

        st.success("🎉 Match!")

        st.session_state.matched_cards.extend(
            [first, second]
        )

        st.session_state.flipped_cards = []

else:

    st.error("❌ Try again")

    time.sleep(1)

    st.session_state.flipped_cards = []

    st.rerun()