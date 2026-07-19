"""
FastAPI Backend
"""

from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File
from fastapi import HTTPException
from api_models import (QuestionRequest,SummaryRequest)
from src.rag_pipeline import rag_query
from src.summarizer import summarize_document
from src.utils import save_uploaded_file
from src.pdf_loader import load_pdfs
from src.chunker import split_documents
from src.vector_db import create_vector_db
app = FastAPI(title="AI Research Assistant API",version="1.0")

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

@app.get("/")
def health():

    return {

        "status": "Running"

    }

