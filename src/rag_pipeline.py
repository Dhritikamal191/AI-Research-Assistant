"""
rag_pipeline.py
----------------
Main Retrieval-Augmented Generation (RAG) Pipeline
"""

from src.retriever import retrieve_documents
from src.prompt import build_prompt
from src.llm import generate_response
from src.hybrid_search import HybridRetriever

def format_context(documents):
    """
    Convert retrieved documents into a prompt-friendly format.
    """

    context = ""

    for i, doc in enumerate(documents, start=1):

        source = doc.metadata.get("source", "Unknown Document")
        page = doc.metadata.get("page", "Unknown")

        context += (
            f"\n========== Chunk {i} ==========\n"
            f"Document: {source}\n"
            f"Page: {page}\n\n"
            f"{doc.page_content}\n\n"
        )

    return context


def rag_query(question, k=5):
    """
    Complete RAG Pipeline

    Parameters
    ----------
    question : str
        User question

    k : int
        Number of retrieved chunks

    Returns
    -------
    dict
    """

    # Retrieve documents

    retriever = HybridRetriever()

    retrieved_docs = retriever.search(question,k=k)

    if len(retrieved_docs) == 0:
        return {
            "answer": "No relevant documents found.",
            "sources": []
        }

    # Build Context
    context = format_context(retrieved_docs)

    # Create Prompt
    prompt = build_prompt(
        context=context,
        question=question
    )

    # Generate Answer
    answer = generate_response(prompt)

    # Extract Sources
    sources = []

    for doc in retrieved_docs:

        sources.append({

            "document": doc.metadata.get(
                "source",
                "Unknown"
            ),

            "page": doc.metadata.get(
                "page",
                "Unknown"
            )

        })

    return {

        "answer": answer,

        "sources": sources,

        "retrieved_chunks": retrieved_docs

    }

def rag_stream(question):

    retrieved_docs = retrieve_documents(question)

    context = format_context(retrieved_docs)

    prompt = build_prompt(
        context,
        question
    )

    return stream_response(prompt)

if __name__ == "__main__":

    question = input("Ask a Question: ")

    result = rag_query(question)

    print("\n========== ANSWER ==========\n")

    print(result["answer"])

    print("\n========== SOURCES ==========\n")

    for src in result["sources"]:

        print(
            f"{src['document']} | Page {src['page']}"
        )