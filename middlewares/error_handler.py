"""Module middleware for manage errors."""
from typing import Any
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class ErrorHandler(BaseHTTPMiddleware):
    """Class handler for manage errors."""

    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Any:
        """Execute calls to routers endpoints.

        Args:
            request (Request): request object.
            call_next (_type_): call endpoint name.

        Returns:
            JSONResponse: _description_
        """
        try:
            return await call_next(request)
        except Exception as e:
            return JSONResponse(status_code=500, content={'error': str(e)})