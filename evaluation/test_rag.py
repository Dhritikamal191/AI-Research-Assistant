import os
import asyncio
import pandas as pd
from openai import AsyncOpenAI
from ragas.embeddings import HuggingFaceEmbeddings
from src.rag_pipeline import rag_query
from ragas.llms import llm_factory
from ragas.metrics.collections import Faithfulness, AnswerRelevancy

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not available.")


# Groq through its OpenAI-compatible API
client = AsyncOpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
)

evaluator_llm = llm_factory(
    "llama-3.3-70b-versatile",
    client=client,
)

completed_questions = set()

async def run_evaluation():

    output_path ="evaluation/results.csv"
    results = []
    os.makedirs("evaluation", exist_ok=True)

    # Run the REAL RAG pipeline
    questions = [
    "What is the main topic of the document?",
    "What qualifications are required?",
    "What is the selection procedure?",
    "What guidelines are given to applicants?",
    "What important dates or deadlines are mentioned?"
   ]

    for question in questions:
        
        if question in completed_questions:
           print(f"\nSkipping completed question: {question}")
           continue

        try:
            print("\n" + "=" * 70)
            print("Evaluating:", question)
            result = rag_query(question)
            answer = result["answer"]
            retrieved_docs = result["retrieved_chunks"]

            contexts = [
               doc.page_content
              for doc in retrieved_docs
            ]

            print("Question:", question)
            print("Answer:", answer)
            print("Retrieved contexts:", len(contexts))

            # Evaluate the real RAG output
            metric = Faithfulness(llm=evaluator_llm)

            score = await metric.ascore(
              user_input=question,
              response=answer,
              retrieved_contexts=contexts,
            )

            print("Faithfulness score:", score)

            evaluator_embeddings = HuggingFaceEmbeddings(
              "sentence-transformers/all-MiniLM-L6-v2"
            )

            relevancy_metric = AnswerRelevancy(
              llm=evaluator_llm,
              embeddings=evaluator_embeddings
              )

            relevancy_score = await relevancy_metric.ascore(
              user_input=question,
              response=answer
            )

            print("Answer Relevancy score:", relevancy_score)

            result_row = {
              "question": question,
              "answer": answer,
              "retrieved_contexts": len(contexts),
              "faithfulness": float(score.value),
              "answer_relevancy": float(relevancy_score.value),
              "status": "completed"
            }

            results.append(result_row)

            # Save immediately after every successful question

            result_df = pd.DataFrame(results).to_csv(output_path, index=False)

            print(f"Checkpoint saved: {len(results)} question(s)")

        except Exception as e:
               print("\nEvaluation interrupted.")
               print("Error:",e)
               print("Previously completed results are preserved.")
               break

    if results:
       df = pd.DataFrame(results)
       os.makedirs("evaluation", exist_ok=True)
       
       print("\n" + "=" * 70)
       print("RAG EVALUATION SUMMARY")
       print("=" * 70)

       output_path = "evaluation/results.csv"
       df.to_csv(output_path, index=False)
       print(f"Questions evaluated: {len(df)}")
       print(f"Average Faithfulness: {df['faithfulness'].mean():.4f}")
       print(f"Average Answer Relevancy: {df['answer_relevancy'].mean():.4f}")
       print(f"Questions completed: {len(df)}/{len(questions)}")
       print(f"Average Faithfulness: {df['faithfulness'].mean():.4f}")
       print(
        f"Average Answer Relevancy: "
        f"{df['answer_relevancy'].mean():.4f}"
       )

       print(f"Results saved to: {output_path}")

       if len(df) == len(questions):
          print("Evaluation completed successfully.")
       else:
            print("Evaluation incomplete — run again later to resume.")

       print(f"\nEvaluation report saved to: {output_path}")

if __name__ == "__main__":
    asyncio.run(run_evaluation())