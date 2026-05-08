from fastapi import APIRouter

from pydantic import BaseModel

from services.conversation_orchestrator import (
    start_session,
    process_message
)

router = APIRouter()


class StartRequest(BaseModel):

    user_id: str


class MessageRequest(BaseModel):

    user_id: str

    message: str


@router.post("/start")

def start_chat(request: StartRequest):

    return start_session(
        request.user_id
    )


@router.post("/message")

def send_message(
    request: MessageRequest
):

    return process_message(

        request.user_id,

        request.message
    )