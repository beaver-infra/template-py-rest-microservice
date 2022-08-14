"""
Holds functions used by Users Sample API
"""

from fastapi import APIRouter, status
from fastapi_versioning import version
from app.models.users import UserModel
from app.mocks.users import mock_users

router = APIRouter(
  prefix="/users",
  tags=["Users"],
  responses={404: {"description": "Not found"}}
)

@router.get("/", status_code=status.HTTP_200_OK)
@version(1)
async def users():
  """
  Return sample response
  """
  return mock_users()

@router.get("/user", status_code=status.HTTP_200_OK)
@version(1)
async def user():
  """
  Return sample response
  """
  return mock_users[0]

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
