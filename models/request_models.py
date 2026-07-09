from pydantic import BaseModel, Field

class QuestionRequest(BaseModel):
    query: str = Field(..., min_length=3)

class ExplainRequest(BaseModel):
    query: str = Field(..., min_length=3)

class SummaryRequest(BaseModel):
    query: str = Field(..., min_length=10)

class RecommendationRequest(BaseModel):
    query: str = Field(..., min_length=3)

class QuizRequest(BaseModel):
    query: str = Field(..., min_length=3)
    number_of_questions: int = Field(default=5, ge=1, le=20)