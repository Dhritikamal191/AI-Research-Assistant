import streamlit as st
from src.streamlit_upload import save_uploaded_file
from src.utils import allowed_file, ensure_directories
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

    if uploaded is not None:

        if st.button("Save PDFs, type="primary"):

            for pdf in uploaded:

                if allowed_file(pdf.name):

                    save_uploaded_file(pdf)

            st.success("Saved Successfully.")

    if st.button("Build Knowledge Base"):

        with st.spinner("Creating FAISS..."):

            docs = load_pdfs()

            if not docs:
                   st.warning("Please upload and save at least one PDF before building the knowledge base.")
                   st.stop()

            chunks = split_documents(docs)

            create_vector_db(chunks)

        st.success("Knowledge Base Created.")