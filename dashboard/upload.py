import streamlit as st

from src.utils import save_uploaded_file
from src.utils import allowed_file

from src.pdf_loader import load_pdfs
from src.chunker import split_documents
from src.vector_db import create_vector_db


def show_upload():

    st.title("📄 Upload Documents")

    uploaded = st.file_uploader(
        "Upload PDF",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded:

        if st.button("Save PDFs"):

            for pdf in uploaded:

                if allowed_file(pdf.name):

                    save_uploaded_file(pdf)

            st.success("Saved Successfully.")

    if st.button("Build Knowledge Base"):

        with st.spinner("Creating FAISS..."):

            docs = load_pdfs()

            chunks = split_documents(docs)

            create_vector_db(chunks)

        st.success("Knowledge Base Created.")