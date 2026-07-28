from pydantic import BaseModel


class QuestionRequest(BaseModel):
    question: str


class SummaryRequest(BaseModel):
    summary_type: str


class CompareRequest(BaseModel):
    document1: str
    document2: str