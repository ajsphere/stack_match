import random
import time
import streamlit as st

from cards import cards
from card_ui import show_card


st.set_page_config(
    page_title="Sweet Match",
    page_icon="🍭"
)


if "game_started" not in st.session_state:
    st.session_state.game_started = False


if not st.session_state.game_started:

    st.title("🍭 Sweet Match")

    st.write(
        "Match all the yummy treats and become the Sweet Match Champion! 🍩🍦🍭"
    )

    if st.button("🎮 Start Game"):

        st.session_state.game_started = True
        st.session_state.start_time = time.time()

        st.rerun()

    st.stop()



st.title("🍭 Sweet Match")

st.caption(
    "Match all the yummy treats and become the Sweet Match Champion! 🍩🍦🍭"
)



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



st.write(
    f"🎯 Attempts: {st.session_state.attempts}"
)


st.write(
    f"🍬 Matches: {len(st.session_state.matched_cards)//2}/{len(game_cards)//2}"
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

            clicked = show_card(
                "",
                index,
                hidden=True
            )


            if clicked:

                st.session_state.flipped_cards.append(index)

                st.rerun()



if len(st.session_state.flipped_cards) == 2:

    first = st.session_state.flipped_cards[0]
    second = st.session_state.flipped_cards[1]


    st.session_state.attempts += 1



    if (
        game_cards[first]["pair"]
        ==
        game_cards[second]["pair"]
    ):

        st.session_state.matched_cards.extend(
            [first, second]
        )

        st.session_state.flipped_cards = []

        st.success("🍭 Sweet Match! 🎉")



    else:

        st.error("😢 Try Again!")

        time.sleep(1)

        st.session_state.flipped_cards = []



    st.rerun()



if len(st.session_state.matched_cards) == len(game_cards):

    elapsed_time = int(
        time.time() - st.session_state.start_time
    )


    st.balloons()


    st.success(
        "🍬 Yum! You Found All the Sweet Treats! 🎉"
    )


    st.write(
        f"⏱️ Time: {elapsed_time} seconds"
    )


    st.write(
        f"🎯 Attempts: {st.session_state.attempts}"
    )


    st.write(
        "🌟 You're a Sweet Match Champion! 🌟"
    )



    if st.button("🔄 Play Again"):

        st.session_state.game_cards = cards.copy()

        random.shuffle(
            st.session_state.game_cards
        )

        st.session_state.flipped_cards = []

        st.session_state.matched_cards = []

        st.session_state.attempts = 0

        st.session_state.start_time = time.time()

        st.rerun()