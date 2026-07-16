import random
import time
import streamlit as st

from cards import cards


st.title("🧠 Stack Match")


if "game_cards" not in st.session_state:
    st.session_state.game_cards = cards.copy()
    random.shuffle(st.session_state.game_cards)

game_cards = st.session_state.game_cards


if "flipped_cards" not in st.session_state:
    st.session_state.flipped_cards = []

if "matched_cards" not in st.session_state:
    st.session_state.matched_cards = []

if "attempts" not in st.session_state:
    st.session_state.attempts = 0


st.write(f"🎯 Attempts: {st.session_state.attempts}")
st.write(
    f"🏆 Matches: {len(st.session_state.matched_cards)//2}/{len(cards)//2}"
)


columns = st.columns(4)


for index, card in enumerate(game_cards):

    with columns[index % 4]:

        if index in st.session_state.matched_cards:

            st.button(
                card["value"],
                key=f"matched_{index}"
            )

        elif index in st.session_state.flipped_cards:

            st.button(
                card["value"],
                key=f"flipped_{index}"
            )

        else:

            if len(st.session_state.flipped_cards) < 2:

                if st.button("🂠", key=f"card_{index}"):

                    st.session_state.flipped_cards.append(index)

                    st.rerun()


if len(st.session_state.flipped_cards) == 2:

    st.session_state.attempts += 1

    first = st.session_state.flipped_cards[0]
    second = st.session_state.flipped_cards[1]


    if game_cards[first]["pair"] == game_cards[second]["pair"]:

        st.success("🎉 Match!")

        st.session_state.matched_cards.extend(
            [first, second]
        )

        st.session_state.flipped_cards = []

        st.rerun()

    else:

        st.error("❌ Try again")

        time.sleep(1)

        st.session_state.flipped_cards = []

        st.rerun()


if len(st.session_state.matched_cards) == len(game_cards):

    st.balloons()
    st.success("🏆 You Win!")