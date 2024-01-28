from typing import List
from pydantic import BaseModel


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    chatHistory: List[Message]
    question: str
    sessionId: int = 12345
