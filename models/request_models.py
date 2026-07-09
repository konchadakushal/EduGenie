from pydantic import BaseModel


class QuestionRequest(BaseModel):
    question: str


class ExplainRequest(BaseModel):
    topic: str


class QuizRequest(BaseModel):
    topic: str
    number_of_questions: int = 5


class SummaryRequest(BaseModel):
    text: str


class RecommendationRequest(BaseModel):
    current_topic: str