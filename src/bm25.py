"""
bm25.py
---------
Keyword Search using BM25
"""

from rank_bm25 import BM25Okapi


class BM25Retriever:

    def __init__(self):

        self.documents = []

        self.tokenized = []

        self.bm25 = None

    def fit(self, docs):

        self.documents = docs

        self.tokenized = [

            d.page_content.lower().split()

            for d in docs

        ]

        self.bm25 = BM25Okapi(self.tokenized)

    def search(self, query, k=10):

        scores = self.bm25.get_scores(

            query.lower().split()

        )

        ranked = sorted(

            zip(scores, self.documents),

            reverse=True,

            key=lambda x: x[0]

        )

        return [

            doc

            for _, doc in ranked[:k]

        ]