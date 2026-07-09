from fastapi import APIRouter
from models.request_models import QuizRequest
from services.gemini_service import generate_response
from models.response_models import ApiResponse

router = APIRouter()

@router.post("/")
def generate_quiz(request: QuizRequest):

    prompt = f"""
    Generate {request.number_of_questions} MCQs on:
    in 200 words
    {request.query}

    Rules:
    - 4 options (A, B, C, D)
    - Mention the correct answer
    - Medium difficulty
    """

    answer = generate_response(prompt)

    return ApiResponse(
    success=True,
    task="Quiz",
    input=request.query,
    output=answer
)