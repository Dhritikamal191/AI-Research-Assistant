"""
reranker.py
------------
Cross Encoder Re-ranking
"""

from sentence_transformers import CrossEncoder

RERANKER_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"

_reranker = None


def get_reranker():

    global _reranker

    if _reranker is None:

        _reranker = CrossEncoder(
            RERANKER_MODEL,
            device="cpu"
        )

    return _reranker


class ReRanker:

    def __init__(self):

        self.model = get_reranker()

    def rerank(
        self,
        query,
        docs,
        top_k=5
    ):

        if not docs:
            return []

        pairs = [
            (
                query,
                d.page_content
            )
            for d in docs
        ]

        scores = self.model.predict(
            pairs,
            show_progress_bar=False
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