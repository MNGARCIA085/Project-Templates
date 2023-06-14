from fastapi import APIRouter

from .endpoints import movies

api_router = APIRouter()
api_router.include_router(movies.router, tags=["movies"])
