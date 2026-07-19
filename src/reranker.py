"""
reranker.py
------------
Cross Encoder Re-ranking
"""

from sentence_transformers import CrossEncoder


class ReRanker:

    def __init__(self):

        self.model = CrossEncoder(

            "cross-encoder/ms-marco-MiniLM-L-6-v2"

        )

    def rerank(

        self,

        query,

        docs,

        top_k=5

    ):

        pairs = [

            (

                query,

                d.page_content

            )

            for d in docs

        ]

        scores = self.model.predict(

            pairs

        )

        ranked = sorted(

            zip(scores, docs),

            reverse=True,

            key=lambda x: x[0]

        )

        return [

            d

            for _, d in ranked[:top_k]

        ]