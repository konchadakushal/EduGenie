from fastapi import APIRouter
from models.request_models import QuestionRequest
from models.response_models import ApiResponse
from services.gemini_service import generate_response

router = APIRouter()


@router.post("/", response_model=ApiResponse)
def question_answer(request: QuestionRequest):

    prompt = f"""
    You are EduGenie.

    Answer the following question:
    in 200 words
    {request.query}

    Include:
    - Definition
    - Explanation
    - Example
    """

    answer = generate_response(prompt)

    return ApiResponse(
        success=True,
        task="Question Answering",
        input=request.query,
        output=answer
    )