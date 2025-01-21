from fastapi import FastAPI

from routers.chat_message import chat_message_router
from routers.user import user_router
from routers.health import health_router
from config.database import engine, Base, Session
from middlewares.error_handler import ErrorHandler
from services.user import UserService


app = FastAPI()
app.title = "Chat GPT API"
app.version = "1.0.0"

app.add_middleware(ErrorHandler)

app.include_router(chat_message_router)
app.include_router(user_router)
app.include_router(health_router)

Base.metadata.create_all(bind=engine)

db = Session()

UserService.initial_migration(db)
