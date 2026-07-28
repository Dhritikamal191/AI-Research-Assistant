"""
utils.py
----------
Utility Functions
"""

import os

UPLOAD_DIR = "data/uploads"

def ensure_directories():
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    os.makedirs("vectorstore", exist_ok=True)
    os.makedirs("logs", exist_ok=True)

def allowed_file(filename):
    return filename.lower().endswith(".pdf")