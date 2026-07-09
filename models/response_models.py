from pydantic import BaseModel


class ApiResponse(BaseModel):
    success: bool
    task: str
    input: str
    output: str