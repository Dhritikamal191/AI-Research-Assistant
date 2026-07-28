import streamlit as st
import os

from src.memory import memory


def show_analytics():

    st.title("📊 Analytics")

    st.metric(
        "Questions Asked",
        len(memory.get_history())
    )

    st.metric(
        "Stored PDFs",
        len(os.listdir("data/uploads"))
        if os.path.exists("data/uploads")
        else 0
    )

    st.metric(
        "Embedding Model",
        "MiniLM"
    )

    st.metric(
        "Vector DB",
        "FAISS"
    )

    st.metric(
        "LLM",
        "Llama 3"
    )