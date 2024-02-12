"""
Defines API routes managed by the service.
"""

from fastapi import APIRouter

from app.endpoints import health, info, users

api_router = APIRouter()

# Include essential routes that all microservices should have and must not be altered.
api_router.include_router(info.router, tags=["info"])
api_router.include_router(health.router, tags=["health"])

# Define microservice-specific routes to handle particular use cases.
# For instance, in this case, it handles user-related functionality.
# It could be adapted for other functionalities like payments, profiles, publishing, carts, etc.
api_router.include_router(users.router, tags=["users"], prefix="/users")
