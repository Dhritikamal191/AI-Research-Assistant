from database.database import SessionLocal
from database.models import ChatHistory


def save_chat(question, answer):

    db = SessionLocal()

    chat = ChatHistory(
        question=question,
        answer=answer
    )

    db.add(chat)

    db.commit()

    db.close()