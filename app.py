import random
import time
import streamlit as st

from cards import cards
from card_ui import show_card


st.set_page_config(
    page_title="Stack Match",
    page_icon="🧠"
)


st.title("🧠 Stack Match")


if "game_cards" not in st.session_state:
    st.session_state.game_cards = cards.copy()
    random.shuffle(st.session_state.game_cards)


if "flipped_cards" not in st.session_state:
    st.session_state.flipped_cards = []


if "matched_cards" not in st.session_state:
    st.session_state.matched_cards = []


if "attempts" not in st.session_state:
    st.session_state.attempts = 0


if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()


if st.button("🔄 Restart Game"):

    st.session_state.game_cards = cards.copy()
    random.shuffle(st.session_state.game_cards)

    st.session_state.flipped_cards = []
    st.session_state.matched_cards = []
    st.session_state.attempts = 0
    st.session_state.start_time = time.time()

    st.rerun()


game_cards = st.session_state.game_cards


st.write(f"🎯 Attempts: {st.session_state.attempts}")

st.write(
    f"🏆 Matches: {len(st.session_state.matched_cards)//2}/{len(game_cards)//2}"
)


columns = st.columns(4)


for index, card in enumerate(game_cards):

    with columns[index % 4]:

        if (
            index in st.session_state.matched_cards
            or index in st.session_state.flipped_cards
        ):

            show_card(
                card["value"],
                index
            )

        else:

            show_card(
                "",
                index,
                hidden=True
            )

            if st.button(
                "🂠",
                key=f"card_{index}"
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

    elapsed_time = int(
        time.time() - st.session_state.start_time
    )

    st.balloons()

    st.success(
        "🌈 Amazing Job! You Found Them All! 🎉"
    )

    st.write(
        f"⏱️ Time: {elapsed_time} seconds"
    )

    st.write(
        f"🎯 Attempts: {st.session_state.attempts}"
    )


    if st.button("🔄 Play Again"):

        st.session_state.game_cards = cards.copy()
        random.shuffle(st.session_state.game_cards)

        st.session_state.flipped_cards = []
        st.session_state.matched_cards = []
        st.session_state.attempts = 0
        st.session_state.start_time = time.time()

        st.rerun()