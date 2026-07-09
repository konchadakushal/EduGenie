from fastapi import APIRouter
from models.request_models import QuizRequest

router = APIRouter()

@router.post("/")
def generate_quiz(request: QuizRequest):

    return {
        "module": "Quiz Generation",
        "topic": request.topic,
        "questions": request.number_of_questions
    }