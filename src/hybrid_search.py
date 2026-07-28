"""
hybrid_search.py
----------------
Hybrid Retrieval
"""

from src.vector_db import load_vector_db
from src.bm25 import BM25Retriever
from src.pdf_loader import load_pdfs
from src.chunker import split_documents
from src.reranker import ReRanker


class HybridRetriever:

    def __init__(self):

        docs = split_documents(

            load_pdfs()

        )

        self.vector = load_vector_db()

        self.keyword = BM25Retriever()

        self.keyword.fit(docs)

        self.reranker = ReRanker()

    def search(

        self,

        question,

        k=5

    ):

        vector_docs = self.vector.similarity_search(

            question,

            k=10

        )

        keyword_docs = self.keyword.search(

            question,

            k=10

        )

        combined = []

        seen = set()

        for doc in vector_docs + keyword_docs:

            key = (

                doc.metadata.get("source"),

                doc.metadata.get("page"),

                doc.page_content[:100]

            )

            if key not in seen:

                seen.add(key)

                combined.append(doc)

        return self.reranker.rerank(

            question,

            combined,

            top_k=k

        )