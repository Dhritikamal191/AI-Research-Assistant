"""
ocr.py
--------
OCR utilities for scanned PDFs and images.
"""

import pytesseract

from PIL import Image

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def image_to_text(image):

    """
    Extract text from a PIL Image.
    """

    return pytesseract.image_to_string(image)