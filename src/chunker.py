"""
chunker.py
-----------
Split documents into chunks.
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    """
    Split documents into chunks.
    """

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=1000,

        chunk_overlap=200,

        separators=[
            "\n\n",
            "\n",
            ".",
            " ",
            ""
        ]

    )

    chunks = splitter.split_documents(documents)

    return chunks