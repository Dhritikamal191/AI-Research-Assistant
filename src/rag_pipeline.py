"""
rag_pipeline.py
----------------
Main Retrieval-Augmented Generation (RAG) Pipeline
"""
from src.cache import response_cache
import time
import logging
from monitoring.logger import log_interaction
from src.prompt import build_prompt
from src.llm import generate_response
from src.hybrid_search import HybridRetriever
from src.reranker import ReRanker
from src.memory import conversation_memory
from src.query_expansion import expand_query
from config import TOP_K

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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


def rag_query(question, k=TOP_K, session_id="default"):

    try:
        start_time = time.time()
    
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
        cached_answer = response_cache.get(question)

        if cached_answer is not None:
           return cached_answer

        if not question or not question.strip():
          return {
        "answer": "Please enter a valid question.",
        "sources": [],
        "context": ""
        }

        history = conversation_memory.get_history(session_id)
        history_text = ""

        for message in history:
            history_text += (
            f"{message['role'].upper()}: "
            f"{message['content']}\n"
            )

        # Retrieve candidate documents using Hybrid Search
        retriever = HybridRetriever()

        # Expand the original question
        expanded_queries = expand_query(question)

        candidate_docs = []

        for query in expanded_queries:
            docs = retriever.search(query, k=k)
            candidate_docs.extend(docs)

        # Deduplicate retrieved documents
        unique_docs = []
        seen = set()

        for doc in candidate_docs:
            key = (
            doc.page_content,
            doc.metadata.get("source"),
            doc.metadata.get("page")
            )

            if key not in seen:
               seen.add(key)
               unique_docs.append(doc)

        retrieved_docs = unique_docs

        if len(candidate_docs) == 0:
           return {
              "answer": "No relevant documents found.",
              "sources": []
             }

        # Rerank hybrid-search results
        reranker = ReRanker()

        retrieved_docs = reranker.rerank(
        query=question,
        docs=candidate_docs,
        top_k=k
        )

        # Build Context
        context = format_context(retrieved_docs)

        # Create Prompt with conversation memory
        if history_text:
           enhanced_context = f"""
        CONVERSATION HISTORY:
        {history_text}

        RETRIEVED DOCUMENT CONTEXT:
        {context}
        """
        else:
             enhanced_context = context

        prompt = build_prompt(
        context=enhanced_context,
        question=question
        )

        # Generate Answer
        answer = generate_response(prompt)

        conversation_memory.add_message(
        session_id,
        "user",
        question
        )

        conversation_memory.add_message(
        session_id,
        "assistant",
        answer
        )

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

        response_time = time.time() - start_time

        log_interaction(
            question=question,
            answer=answer,
            retrieved_chunks=len(retrieved_docs),
            response_time=response_time
        )

        response_cache.set(question, answer)

    except Exception as e:
           logger.exception("RAG pipeline failed")

        return {
            "answer": "Please upload a document before asking questions.",
            "sources": [],
            "context": "",
            "retrieved_chunks": []
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