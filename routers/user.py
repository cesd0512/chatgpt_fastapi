from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.encoders import jsonable_encoder
from utils.jwt_manager import create_token
from fastapi.responses import JSONResponse
from schemas.user import User
from config.database import Session
from services.user import UserService
from middlewares.jwt_bearer import JWTBearer


user_router = APIRouter()


@user_router.post('/login', tags=['auth'])
def login(user: User) -> JSONResponse:
    "Start session with user."
    db = Session()
    user_service = UserService(db)
    user_db = user_service.validate_user(username=user.username, password=user.password)
    if user_db:
        token: str = create_token(jsonable_encoder(user_db))
        return JSONResponse(
            status_code=200,
            content={'token': token}
        )

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Invalid username or password",
    )


@user_router.post('/init_user', tags=['auth'])
def init_user(user: User) -> JSONResponse:
    """Register new user in database."""
    db = Session()
    user_service = UserService(db)
    user_db = user_service.create_user(user)
    return JSONResponse(
        status_code=200,
        content={'msg': 'User created successful', 'user_id': user_db.id}
    )
