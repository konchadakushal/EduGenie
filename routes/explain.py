from fastapi import APIRouter
from models.request_models import ExplainRequest
from services.gemini_service import generate_response
from models.response_models import ApiResponse

router = APIRouter()

@router.post("/")
def explain(request: ExplainRequest):

    prompt = f"""
    Explain the following topic in a simple and beginner-friendly way.
    in 200 words
    Topic:
    {request.query}

    Include:
    - Definition
    - Working
    - Example
    """

    answer = generate_response(prompt)

    return ApiResponse(
    success=True,
    task="Explanation",
    input=request.query,
    output=answer
)