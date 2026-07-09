from fastapi import FastAPI

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

app.include_router(qa.router, prefix="/qa", tags=["Question Answering"])
app.include_router(explain.router, prefix="/explain", tags=["Explanation"])
app.include_router(quiz.router, prefix="/quiz", tags=["Quiz"])
app.include_router(summarize.router, prefix="/summarize", tags=["Summarization"])
app.include_router(recommend.router, prefix="/learn", tags=["Learning Path"])

@app.get("/")
def home():
    return {
        "message": "Welcome to EduGenie!"
    }