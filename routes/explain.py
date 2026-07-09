from fastapi import APIRouter
from models.request_models import ExplainRequest

router = APIRouter()

@router.post("/")
def explain(request: ExplainRequest):

    return {
        "module": "Concept Explanation",
        "topic": request.topic,
        "explanation": "Explanation will come from Gemini."
    }