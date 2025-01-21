from services.user import UserService
from models.chat_message import ChatMessage as ChatMessageModel
from schemas.chat_message import ChatMessage as ChatMessageSchema


class ChatMessageService():
    """Class service for build operations in db for table chat_message."""

    def __init__(self, db) -> None:
        self.db = db

    def create_message(self, message: ChatMessageSchema) -> int:
        """Method for create chat message in model db."""
        new_message = ChatMessageModel(**message.dict())
        self.db.add(new_message)
        self.db.commit()
        return new_message.id # type: ignore

    def get_messages_by_user(self, username: str) -> ChatMessageModel:
        """Method for get messages's user."""
        user_db = UserService(self.db).get_user(username)
        return self.db.query(ChatMessageModel).filter(
            ChatMessageModel.user_id == user_db.id).all()
