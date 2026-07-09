from fastapi import APIRouter
from models.request_models import RecommendationRequest

router = APIRouter()

@router.post("/")
def recommend(request: RecommendationRequest):

    return {
        "module": "Learning Recommendation",
        "current_topic": request.current_topic,
        "recommendation": [
            "Arrays",
            "Strings",
            "OOP",
            "Collections"
        ]
    }