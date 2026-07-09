from fastapi import APIRouter
from models.request_models import SummaryRequest

router = APIRouter()

@router.post("/")
def summarize(request: SummaryRequest):

    return {
        "module": "Summarization",
        "summary": "Summary will come from LaMini-Flan-T5."
    }