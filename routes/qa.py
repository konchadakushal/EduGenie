from fastapi import APIRouter
from models.request_models import QuestionRequest
from services.gemini_service import generate_response

router = APIRouter()

@router.post("/")
def question_answer(request: QuestionRequest):

    prompt = f"""
You are EduGenie, an AI Educational Assistant.

Answer the following question in a simple and beginner-friendly way.

Question:
{request.question}

Give:
1. Definition
2. Explanation
3. Example
"""

    answer = generate_response(prompt)

    return {
        "question": request.question,
        "answer": answer
    }