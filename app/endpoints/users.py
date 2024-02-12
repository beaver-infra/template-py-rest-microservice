"""
Contains endpoints for the Users Sample API.
"""

import requests
from fastapi import APIRouter, status
from fastapi_versioning import version

from app.core import common_handlers
from app.models.users import UserModel

# Initialize API router
router = APIRouter(
    prefix="/users", tags=["Users"], responses={404: {"description": "Not found"}}
)

# Load configuration settings
CONFIG = common_handlers.load_config()
# Define base URL for downstream services
BASE_URL = CONFIG.DOWNSTREAMS.JSON_PLACE_HOLDER


@router.get("/", status_code=status.HTTP_200_OK)
@version(1)
async def get_users():
    """
    Endpoint to retrieve a list of users.
    Returns:
        JSON response containing user data.
    """
    response = requests.get(f"{BASE_URL}/users", timeout=10)
    if response.status_code == status.HTTP_200_OK:
        return response.json()
    return None


@router.get("/{user_id}", status_code=status.HTTP_200_OK)
@version(1)
async def get_user(user_id: int):
    """
    Endpoint to retrieve a specific user by ID.
    Args:
        user_id (int): The ID of the user to retrieve.
    Returns:
        JSON response containing user data.
    """
    response = requests.get(f"{BASE_URL}/users/{user_id}", timeout=10)
    if response.status_code == status.HTTP_200_OK:
        return response.json()
    return None


@router.post("/user", status_code=status.HTTP_200_OK)
@version(1)
async def add_user(user: UserModel):
    """
    Endpoint to add a new user.
    Args:
        user (UserModel): The user object to add.
    Returns:
        JSON response confirming the addition of the user.
    """
    return {
        "user_id": user.user_id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
    }
