"""
Holds all API routes hosted by the service
"""

from fastapi import APIRouter
from app.endpoints import info, health, users

api_router = APIRouter()

# Special routes which all the microservice should have and should not be removed or disturbed
api_router.include_router(info.router)
api_router.include_router(health.router)

# Microservice routes specific to handler the use case.
# For example, here its users similar it could be payments, profile, publish, cart etc.
api_router.include_router(users.router)
