"""
Import the APIRouter class from the FastAPI framework
"""

from fastapi import APIRouter

# Import the endpoint routers for health, information, and user functionalities
from app.endpoints import health, info, users

# Create an APIRouter instance to hold all API routes hosted by the service
api_router = APIRouter()

# Include special routes that all microservices should have and must not be altered
api_router.include_router(info.router)  # Information endpoint
api_router.include_router(health.router)  # Health check endpoint

# Include microservice-specific routes to handle different use cases,
# such as user management, payments, profiles, publishing, and cart functionalities
api_router.include_router(users.router)  # User management endpoint
