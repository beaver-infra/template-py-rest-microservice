from fastapi import APIRouter
from api.routers import users

api_router = APIRouter()

api_router.include_router(users.router, tags=["users"], prefix="/users")
