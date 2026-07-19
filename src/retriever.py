"""
retriever.py
------------
Semantic Document Retriever
"""

from src.vector_db import load_vector_db


def retrieve_documents(question, k=5):
    """
    Retrieve Top K Relevant Documents
    """

    vector_db = load_vector_db()

    docs = vector_db.similarity_search(
        question,
        k=k
    )

    return docs