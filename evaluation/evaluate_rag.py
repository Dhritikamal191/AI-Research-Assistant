import os
import asyncio
from openai import AsyncOpenAI

from ragas.llms import llm_factory
from ragas.metrics.collections import Faithfulness


GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not available.")


# Groq OpenAI-compatible async client
client = AsyncOpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
)

evaluator_llm = llm_factory(
    "llama-3.3-70b-versatile",
    client=client,
)


async def run_evaluation():

    sample = {
        "user_input": "What is Retrieval-Augmented Generation?",
        "response": (
            "Retrieval-Augmented Generation combines information retrieval "
            "with a language model to generate answers using retrieved context."
        ),
        "retrieved_contexts": [
            (
                "Retrieval-Augmented Generation (RAG) retrieves relevant "
                "information from an external knowledge source and provides "
                "that information to a language model when generating an answer."
            )
        ],
    }

    metric = Faithfulness(llm=evaluator_llm)

    score = await metric.ascore(
        user_input=sample["user_input"],
        response=sample["response"],
        retrieved_contexts=sample["retrieved_contexts"],
    )

    print("Faithfulness score:", score)


if __name__ == "__main__":
    asyncio.run(run_evaluation())