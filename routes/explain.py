from fastapi import APIRouter
from models.request_models import ExplainRequest
from services.gemini_service import generate_response

router = APIRouter()

@router.post("/")
def explain(request: ExplainRequest):

    prompt = f"""
    Explain the following topic in a simple and beginner-friendly way.

    Topic:
    {request.query}

    Include:
    - Definition
    - Working
    - Example
    """

    explanation = generate_response(prompt)

    return ApiResponse(
    success=True,
    task="Explanation",
    input=request.query,
    output=answer
)