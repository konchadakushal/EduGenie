from fastapi import FastAPI
from utils.exception_handler import global_exception_handler
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import HTMLResponse


from routes import (
    qa,
    explain,
    quiz,
    summarize,
    recommend
)

app = FastAPI(
    title="EduGenie API",
    version="1.0.0",
    description="AI-Powered Educational Assistant"
)


# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

app.include_router(qa.router, prefix="/qa", tags=["Question Answering"])
app.include_router(explain.router, prefix="/explain", tags=["Explanation"])
app.include_router(quiz.router, prefix="/quiz", tags=["Quiz"])
app.include_router(summarize.router, prefix="/summarize", tags=["Summarization"])
app.include_router(recommend.router, prefix="/learn", tags=["Learning Path"])

from fastapi import Request
from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )