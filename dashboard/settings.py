import streamlit as st

from src.memory import memory


def show_settings():

    st.title("⚙ Settings")

    temperature = st.slider(

        "Temperature",

        0.0,

        1.0,

        0.3

    )

    top_k = st.slider(

        "Top K Retrieval",

        1,

        10,

        5

    )

    if st.button("Clear Chat"):

        memory.clear()

        st.success("Chat Cleared")

    st.info(

        f"""
Temperature : {temperature}

Top K : {top_k}
"""
    )