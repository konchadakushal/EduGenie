from fastapi import APIRouter
from models.request_models import SummaryRequest
from services.gemini_service import generate_response
from models.response_models import ApiResponse

router = APIRouter()

@router.post("/")
def summarize(request: SummaryRequest):

    prompt = f"""
    Summarize the following content into concise bullet points.
    in 200 words
    Text:
    {request.query}
    """

    answer = generate_response(prompt)

    return ApiResponse(
    success=True,
    task="Text Summarization",
    input=request.query,
    output=answer
)