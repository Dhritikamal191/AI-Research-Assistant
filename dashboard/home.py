import streamlit as st
import os

from src.memory import memory


def show_home():

    st.title("📚 AI Research Assistant")

    st.markdown(
        """
AI-powered Research Assistant using

- Llama 3
- LangChain
- FAISS
- HuggingFace Embeddings
"""
    )

    col1, col2, col3, col4 = st.columns(4)

    pdfs = 0

    if os.path.exists("data/uploads"):

        pdfs = len([
            f for f in os.listdir("data/uploads")
            if f.endswith(".pdf")
        ])

    history = len(memory.get_history())

    chunks = 0

    if os.path.exists("vectorstore/faiss_index/index.faiss"):
        chunks = "Available"

    with col1:
        st.metric("PDFs", pdfs)

    with col2:
        st.metric("Chat History", history)

    with col3:
        st.metric("Knowledge Base", chunks)

    with col4:
        st.metric("LLM", "Llama 3")

    st.divider()

    st.subheader("Project Features")

    st.markdown("""
✅ Multi PDF Upload

✅ RAG Search

✅ AI Chat

✅ Summaries

✅ Document Comparison

✅ Source Citation

✅ Feedback Logging

✅ Conversation Memory
""")