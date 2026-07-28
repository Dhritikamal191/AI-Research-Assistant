import streamlit as st

from src.pdf_loader import load_pdfs
from src.summarizer import summarize_document


def show_summary():

    st.title("📝 Summarizer")

    option = st.selectbox(

        "Summary Type",

        [

            "Executive",

            "Detailed",

            "Bullet",

            "Key Findings"

        ]

    )

    if st.button("Generate"):

        docs = load_pdfs()

        text = "\n".join(

            d.page_content

            for d in docs

        )

        summary = summarize_document(
            text,
            option
        )

        st.write(summary)