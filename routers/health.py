from fastapi import APIRouter
from fastapi.responses import JSONResponse
from config.database import engine
from sqlalchemy import text


health_router = APIRouter()


@health_router.get('/health', tags=['health'])
def health() -> JSONResponse:
    """Validates service status and connection to database."""
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return JSONResponse(
            status_code=200,
            content={
                'msg': 'Connection successful.',
                'status': 'ok'
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code=200,
            content={
                'msg': f"Database connection failed: {e}",
                'status': 'error'
            }
        )

