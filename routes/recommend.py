from fastapi import APIRouter
from models.request_models import RecommendationRequest
from services.gemini_service import generate_response

router = APIRouter()

@router.post("/")
def recommend(request: RecommendationRequest):

    prompt = f"""
    A student has completed:

    {request.query}

    Recommend:
    - Next topics
    - Learning order
    - Practice websites
    - Free resources
    """

    recommendation = generate_response(prompt)

    return ApiResponse(
    success=True,
    task="Recommendation",
    input=request.query,
    output=answer
)