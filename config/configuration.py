import os
from passlib.context import CryptContext
from dotenv import load_dotenv


load_dotenv()

SECRET_KEY = os.environ['SECRET_KEY']

PWD_ADMIN = os.environ['PWD_ADMIN']

# Hasheo de contraseñas
PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")

ROLES = [
    "Administrador",
    "User"
]

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']