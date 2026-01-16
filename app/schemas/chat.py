from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    question: str = Field(..., min_length=3, example="What is the current status of Air India?")


class ChatResponse(BaseModel):
    answer: str
