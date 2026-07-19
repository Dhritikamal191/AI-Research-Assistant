"""
utils.py
----------
Utility Functions
"""

import os
import shutil

UPLOAD_DIR = "data/uploads"


def ensure_directories():

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    os.makedirs("vectorstore", exist_ok=True)

    os.makedirs("logs", exist_ok=True)


async def save_uploaded_file(uploaded_file):

          ensure_directories()

          save_path = os.path.join(UPLOAD_DIR,uploaded_file.filename)

          with open(save_path, "wb") as f:

               contents = await uploaded_file.read()
               f.write(contents)

          return save_path


def allowed_file(filename):

    return filename.lower().endswith(".pdf")