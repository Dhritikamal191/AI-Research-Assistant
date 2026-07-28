"""
create_index.py
"""

from src.pdf_loader import load_pdfs
from src.chunker import split_documents
from src.vector_db import create_vector_db


print("Loading PDFs...")

documents = load_pdfs()

print(f"{len(documents)} pages loaded.")

print("Chunking...")

chunks = split_documents(documents)

print(f"{len(chunks)} chunks created.")

print("Creating FAISS...")

create_vector_db(chunks)

print("Done!")

print("FAISS Index Saved Successfully.")