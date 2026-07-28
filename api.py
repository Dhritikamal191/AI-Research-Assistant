"""
FastAPI Backend
"""
import os
import pandas as pd
from fastapi import HTTPException
from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File
from fastapi import HTTPException
from api_models import (QuestionRequest,SummaryRequest)
from src.rag_pipeline import rag_query
from src.summarizer import summarize_document
from src.fastapi_upload import save_uploaded_file
from src.utils import ensure_directories
from src.pdf_loader import load_pdfs
from src.chunker import split_documents
from src.vector_db import create_vector_db
app = FastAPI(
    title="AI Research Assistant API",
    description="A Retrieval-Augmented Generation (RAG) system with Hybrid Search, Query Expansion, Conversation Memory, Cross-Encoder Reranking, Evaluation and Monitoring.",
    version="1.0.0"
)

@app.get("/health")
def health_check():

    return {

        "status": "healthy",
        "service": "AI Research Assistant API"

    }

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename.endswith(".pdf"):

        raise HTTPException(status_code=400,detail="Only PDF allowed.")

    await save_uploaded_file(file)

    docs = load_pdfs()

    chunks = split_documents(docs)

    create_vector_db(chunks)

    return {

        "message": "Knowledge Base Updated"

    }

@app.post("/chat")
def chat(data: QuestionRequest):

    result = rag_query(data.question)

    return {

        "question": data.question,

        "answer": result["answer"],

        "sources": result["sources"]

    }

@app.post("/summary")
def summary(data: SummaryRequest):

    docs = load_pdfs()

    text = "\n".join(

        d.page_content

        for d in docs

    )

    result = summarize_document(
        text,
        data.summary_type
    )

    return {

        "summary": result

    }

@app.get("/evaluation")
def get_evaluation_metrics():

    results_file = "evaluation/results.csv"

    if not os.path.exists(results_file):
        return {
            "status": "no_data",
            "message": "No RAG evaluation results available."
        }

    if os.path.getsize(results_file) == 0:
        return {
            "status": "no_data",
            "message": "RAG evaluation results are currently empty."
        }

    try:
        df = pd.read_csv(results_file)

        if df.empty:
            return {
                "status": "no_data",
                "message": "No completed evaluations available."
            }

        avg_faithfulness = df["faithfulness"].mean()
        avg_relevancy = df["answer_relevancy"].mean()

        overall_score = (
            avg_faithfulness + avg_relevancy
        ) / 2

        return {
            "status": "success",
            "questions_evaluated": len(df),
            "average_faithfulness": round(
                float(avg_faithfulness), 4
            ),
            "average_answer_relevancy": round(
                float(avg_relevancy), 4
            ),
            "overall_rag_score": round(
                float(overall_score), 4
            )
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Could not read evaluation results: {str(e)}"
        )