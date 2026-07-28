import os
import csv
from datetime import datetime, timezone

LOG_FILE = "monitoring/rag_interactions.csv"


def log_interaction(
    question,
    answer,
    retrieved_chunks,
    response_time
):
    os.makedirs("monitoring", exist_ok=True)

    file_exists = os.path.exists(LOG_FILE)

    with open(
        LOG_FILE,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "question",
                "answer",
                "retrieved_chunks",
                "response_time_seconds"
            ])

        writer.writerow([
            datetime.now(timezone.utc).isoformat(),
            question,
            answer,
            retrieved_chunks,
            round(response_time, 3)
        ])

FEEDBACK_FILE = "monitoring/user_feedback.csv"

def log_feedback(question, answer, feedback):
    os.makedirs("monitoring", exist_ok=True)

    file_exists = os.path.exists(FEEDBACK_FILE)

    with open(
        FEEDBACK_FILE,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "question",
                "answer",
                "feedback"
            ])

        writer.writerow([
            datetime.now(timezone.utc).isoformat(),
            question,
            answer,
            feedback
        ])