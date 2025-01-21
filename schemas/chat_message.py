from pydantic import BaseModel


class ChatMessage(BaseModel):
    """Scheme for model ChatMessage."""
    id: str
    message: str
    response: str
    user_id: int
