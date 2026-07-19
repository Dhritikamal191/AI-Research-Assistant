"""
feedback.py
-----------
Stores user feedback for RAG responses.
"""

import csv
import os
from datetime import datetime

FEEDBACK_DIR = "artifacts"
FEEDBACK_FILE = os.path.join(FEEDBACK_DIR, "feedback.csv")


def initialize_feedback():

    os.makedirs(FEEDBACK_DIR, exist_ok=True)

    if not os.path.exists(FEEDBACK_FILE):

        with open(FEEDBACK_FILE, "w", newline="", encoding="utf-8") as f:

            writer = csv.writer(f)

            writer.writerow([
                "Timestamp",
                "Question",
                "Answer",
                "Rating"
            ])


def save_feedback(question, answer, rating):

    initialize_feedback()

    with open(
        FEEDBACK_FILE,
        "a",
        newline="",
        encoding="utf-8"
    ) as f:

        writer = csv.writer(f)

        writer.writerow([
            datetime.now(),
            question,
            answer,
            rating
        ])