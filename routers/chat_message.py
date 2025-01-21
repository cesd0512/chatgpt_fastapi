import uuid
from fastapi import Depends, APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from config.database import Session
from middlewares.jwt_bearer import JWTBearer
from services.chat_message import ChatMessageService
from services.user import UserService
from schemas.chat_message import ChatMessage as ChatMessageSchema
from utils.openai_conn import openai_chat_message


chat_message_router = APIRouter()


@chat_message_router.get('/chat_messages/history/{username}', tags=['messages'],
                         response_model=dict, status_code=200,
                         dependencies=[Depends(JWTBearer())])
def get_messages_by_user(username: str) -> JSONResponse:
    """Endpoint for get messages's user."""
    db = Session()
    result = ChatMessageService(db).get_messages_by_user(username)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@chat_message_router.post('/chat_messages/ask', tags=['messages'],
                   response_model=dict, status_code=201,
                   dependencies=[Depends(JWTBearer())])
def create_message(username: str, message: str) -> JSONResponse:
    "Endpoint for create and save message."
    db = Session()

    user_db = UserService(db).get_user(username)
    response_openai = openai_chat_message(message)

    unique_id = uuid.uuid4()
    unique_id_str = str(unique_id)

    chat_message = ChatMessageSchema(
        id=unique_id_str,
        message=message,
        response=response_openai,
        user_id=user_db.id # type: ignore
    )

    message_id = ChatMessageService(db).create_message(chat_message)

    return JSONResponse(
        status_code=201,
        content={
            "message": "Message saved successful",
            "message_id": message_id,
            "response": response_openai
        })
