"""
Holds functions used by Users Sample API
"""

from fastapi import APIRouter, status
from fastapi_versioning import version
from app.models.users import UserModel
import requests

router = APIRouter(
  prefix="/users",
  tags=["Users"],
  responses={404: {"description": "Not found"}}
)

@router.get("/", status_code=status.HTTP_200_OK)
@version(1)
async def get_users():
  """
  Return sample response
  """
  response = requests.get(f"https://jsonplaceholder.typicode.com/users")
  if response.status_code == status.HTTP_200_OK:
    return response.json()
  else:
    return None

@router.get("/{user_id}", status_code=status.HTTP_200_OK)
@version(1)
async def get_user(user_id: int):
  """
  Return sample response
  """
  response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
  if response.status_code == status.HTTP_200_OK:
    return response.json()
  else:
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
    "email": user.email
  }
