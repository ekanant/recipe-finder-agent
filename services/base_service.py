from models.chat_request import ChatRequest
from models.chat_response import ChatResponse


class BaseService:
    def execute(self, request: ChatRequest) -> ChatResponse:
        """Overrides chat() here"""
        pass
