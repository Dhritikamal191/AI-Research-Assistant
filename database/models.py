from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy.sql import func
from datetime import datetime
from database.database import Base

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
 
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class ChatHistory(Base):

    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)

    question = Column(Text, nullable=False)

    answer = Column(Text, nullable=False)

    created_at = Column(DateTime,default=datetime.utcnow)

    timestamp = Column(DateTime(timezone=True), server_default=func.now())

class Feedback(Base):

    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)

    question = Column(Text)

    answer = Column(Text)

    rating = Column(Integer)

    comments = Column(Text)

    created_at = Column(DateTime,default=datetime.utcnow)

    timestamp = Column(DateTime(timezone=True), server_default=func.now())

class UploadedDocument(Base):

    __tablename__ = "uploaded_documents"

    id = Column(Integer, primary_key=True, index=True)
   
    filename = Column(String(255), nullable=False)

    pages = Column(Integer)

    upload_time = Column(DateTime(timezone=True), server_default=func.now())
   
    vector_status = Column(String(50), default="Indexed")

class EvaluationResult(Base):

    __tablename__ = "evaluation_results"

    id = Column(Integer, primary_key=True, index=True)
   
    question = Column(Text)
  
    answer = Column(Text)
 
    faithfulness = Column(Float)

    answer_relevency = Column(Float)

    context_precision = Column(Float)

    context_recall = Column(Float)

    timestamp = Column(DateTime(timezone=True), server_default=func.now())