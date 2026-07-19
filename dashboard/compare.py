import streamlit as st

from src.compare_docs import compare_documents
from src.pdf_loader import load_pdfs


def show_compare():

    st.title("📚 Compare Documents")

    if st.button("Compare"):

        docs = load_pdfs()

        documents = {}

        for doc in docs:

            src = doc.metadata["source"]

            if src not in documents:

                documents[src] = ""

            documents[src] += doc.page_content

        result = compare_documents(documents)

        st.write(result)