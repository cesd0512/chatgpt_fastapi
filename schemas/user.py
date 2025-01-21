from typing import Optional
from pydantic import BaseModel


class Rol(BaseModel):
    id: Optional[int] = None
    name:str


class User(BaseModel):
    id: Optional[int] = None
    username:str
    password:str
    rol_id: Optional[int] = 2

    class Config:
        schema_extra = {
            "example": {
                "username": "Chat gpt saludo.",
                "password": "Chat gpt saludo."
            }
        }
