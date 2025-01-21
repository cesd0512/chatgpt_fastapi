from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base


class ChatMessage(Base):
    """Model chat messages in db."""

    __tablename__ = "chat_messages"

    id = Column(String, primary_key=True, index=True)
    message = Column(String, unique=True, nullable=False)
    response = Column(String, unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    user = relationship("User", back_populates="messages")
