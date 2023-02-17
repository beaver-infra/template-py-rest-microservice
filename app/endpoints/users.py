"""
Holds functions used by Users Sample API
"""

import requests
from fastapi import APIRouter, status
from fastapi_versioning import version
from app.models.users import UserModel
from app.core import common_handlers

router = APIRouter(
    prefix="/users", tags=["Users"], responses={404: {"description": "Not found"}}
)

configs = common_handlers.get_instance_type_configs()
baseUrl = configs.DOWNSTREAM_CONNECT["JSON_PLACE_HOLDER"]


@router.get("/", status_code=status.HTTP_200_OK)
@version(1)
async def get_users():
    """
    Return sample response
    """
    response = requests.get(f"{baseUrl}/users", timeout=10)
    if response.status_code == status.HTTP_200_OK:
        return response.json()
    return None


@router.get("/{user_id}", status_code=status.HTTP_200_OK)
@version(1)
async def get_user(user_id: int):
    """
    Return sample response
    """
    response = requests.get(f"{baseUrl}/users/{user_id}", timeout=10)
    if response.status_code == status.HTTP_200_OK:
        return response.json()
    return None


@router.post("/user", status_code=status.HTTP_200_OK)
@version(1)
async def add_user(user: UserModel):
    """
    Return sample response
    """
    return {
        "user_id": user.user_id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
    }
