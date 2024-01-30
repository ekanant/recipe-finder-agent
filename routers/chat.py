from typing import Annotated
from fastapi import Depends, APIRouter, Response

from models.chat_request import ChatRequest
from services.base_service import BaseService
from services.chat_service import ChatService

router = APIRouter(
    prefix="/chat",
    tags=["chat"],
    responses={404: {"description": "Not found"}},
)


@router.post("")
async def chat(request: ChatRequest, chat_service: Annotated[BaseService, Depends(ChatService)]):
    #TODO: 1
    response = chat_service.execute(request=request)

    return Response(str(response))
