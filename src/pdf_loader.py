"""
pdf_loader.py
--------------
Loads one or more PDF files using PyMuPDF.
"""

import os
import fitz

from langchain_core.documents import Document
from PIL import Image
from src.ocr import image_to_text

def load_pdfs(upload_folder="data/uploads"):
    """
    Load all PDFs from upload folder.

    Returns
    -------
    list[Document]
    """

    documents = []

    if not os.path.exists(upload_folder):
        raise FileNotFoundError(
            f"{upload_folder} does not exist."
        )

    pdf_files = [
        f for f in os.listdir(upload_folder)
        if f.lower().endswith(".pdf")
    ]

    if len(pdf_files) == 0:
        raise ValueError("No PDF files found.")

    for pdf in pdf_files:

        pdf_path = os.path.join(upload_folder, pdf)

        pdf_file = fitz.open(pdf_path)

        for page_num in range(len(pdf_file)):

            page = pdf_file.load_page(page_num)

            text = page.get_text()

            if not text.strip():

               pix = page.get_pixmap()

               image = Image.frombytes("RGB",[pix.width, pix.height],pix.samples)

               text = image_to_text(image)

            if text.strip():

                documents.append(

                    Document(

                        page_content=text,

                        metadata={
                            "source": pdf,
                            "page": page_num + 1
                        }

                    )

                )

        pdf_file.close()

    return documents