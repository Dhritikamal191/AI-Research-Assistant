"""
config.py
-----------
Application Configuration
"""

from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
UPLOAD_DIR = DATA_DIR / "uploads"

VECTOR_DB_DIR = BASE_DIR / "vectorstore"
FAISS_DIR = VECTOR_DB_DIR / "faiss_index"

LOG_DIR = BASE_DIR / "logs"

ARTIFACT_DIR = BASE_DIR / "artifacts"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

LLM_MODEL = "llama-3.3-70b-versatile"

CHUNK_SIZE = 1000

CHUNK_OVERLAP = 200

TOP_K = 5

TEMPERATURE = 0.3

MAX_TOKENS = 1024

API_KEY = os.getenv("GROQ_API_KEY")