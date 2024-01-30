from models.chat_request import ChatRequest
from services.base_service import BaseService


class ChatService(BaseService):

    def execute(self, request: ChatRequest):
        # TODO: 2.1 - To create a tools for agent
        # TODO: 2.2 - To create an agent
        # TODO: 2.3 - Create prompt template (which included chatHistory)
        # TODO: 2.4 - Invoke an agent
        return "Mock Response"
