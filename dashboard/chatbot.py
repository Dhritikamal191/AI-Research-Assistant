import streamlit as st
from src.rag_pipeline import rag_query
from src.memory import memory


def show_chatbot():

    st.title("💬 Chat")

    question = st.chat_input("Ask anything...")

    if question:

        with st.chat_message("user"):

            st.write(question)

        result = rag_query(question)

        memory.add(
            question,
            result["answer"]
        )

        with st.chat_message("assistant"):

            placeholder = st.empty()

            placeholder.markdown (result["answer"])                

            st.markdown(result["answer"])

            for source in result["sources"]:

                st.write(
                    f"📄 {source['document']} | Page {source['page']}"
                )