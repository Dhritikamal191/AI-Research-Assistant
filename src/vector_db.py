"""
vector_db.py
------------
Create, Save and Load FAISS Vector Database
"""

import os

from langchain_community.vectorstores import FAISS

from src.embeddings import get_embeddings

VECTOR_DB_PATH = "vectorstore/faiss_index"


def create_vector_db(documents):
    """
    Create FAISS Vector Database
    """

    embeddings = get_embeddings()

    vector_db = FAISS.from_documents(
        documents,
        embeddings
    )

    vector_db.save_local(VECTOR_DB_PATH)

    return vector_db


def load_vector_db():
    """
    Load Existing Vector Database
    """

    if not os.path.exists(VECTOR_DB_PATH):

        raise FileNotFoundError(
            "FAISS database not found. Please process documents first."
        )

    embeddings = get_embeddings()

    vector_db = FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_db