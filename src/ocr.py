"""
ocr.py
--------
OCR utilities for scanned PDFs and images.
"""

import pytesseract
import platform
from PIL import Image
import shutil
if platform.system() == "Windows":
    windows_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    if shutil.which("tesseract") is None:
        pytesseract.pytesseract.tesseract_cmd = windows_path

def image_to_text(image):

    """
    Extract text from a PIL Image.
    """

    return pytesseract.image_to_string(image)