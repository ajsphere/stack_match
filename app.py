import random
import time
import streamlit as st

from cards import cards
from card_ui import show_card


st.set_page_config(
    page_title="Stack Match",
    page_icon="🧠"
)


st.markdown(
    """
    <style>
    .card {
        background-color: #ffffff;
        border-radius: 15px;
        height: 90px;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 45px;
        border: 2px solid #dddddd;
        margin: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("🧠 Stack Match")


if st.button("🔄 Restart Game"):

    st.session_state.game_cards = cards.copy()
    random.shuffle(st.session_state.game_cards)

    st.session_state.flipped_cards = []
    st.session_state.matched_cards = []
    st.session_state.attempts = 0

    st.rerun()


if "game_cards" not in st.session_state:
    st.session_state.game_cards = cards.copy()
    random.shuffle(st.session_state.game_cards)


if "flipped_cards" not in st.session_state:
    st.session_state.flipped_cards = []


if "matched_cards" not in st.session_state:
    st.session_state.matched_cards = []


if "attempts" not in st.session_state:
    st.session_state.attempts = 0


game_cards = st.session_state.game_cards


st.write(f"🎯 Attempts: {st.session_state.attempts}")
st.write(
    f"🏆 Matches: {len(st.session_state.matched_cards)//2}/{len(game_cards)//2}"
)


columns = st.columns(4)


for index, card in enumerate(game_cards):

    with columns[index % 4]:

        if index in st.session_state.matched_cards or index in st.session_state.flipped_cards:

            st.button(
                card["value"],
                key=f"open_{index}"
            )

        else:

            if st.button(
                "🂠",
                key=f"closed_{index}"
            ):

                st.session_state.flipped_cards.append(index)

                st.rerun()


if len(st.session_state.flipped_cards) == 2:

    first = st.session_state.flipped_cards[0]
    second = st.session_state.flipped_cards[1]

    st.session_state.attempts += 1


    if game_cards[first]["pair"] == game_cards[second]["pair"]:

        st.session_state.matched_cards.extend(
            [first, second]
        )

        st.session_state.flipped_cards = []

        st.success("🎉 Match!")


    else:

        st.error("❌ Try again")

        time.sleep(1)

        st.session_state.flipped_cards = []


    st.rerun()


if len(st.session_state.matched_cards) == len(game_cards):

    st.balloons()
    st.success("🏆 You Win!")