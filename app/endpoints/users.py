"""
Holds functions used by Users Sample API
"""

from fastapi import APIRouter
from fastapi_versioning import version
from app.models.users import UserModel

# router = APIRouter()

router = APIRouter(
  prefix="/users",
  tags=["Users"],
  responses={404: {"description": "Not found"}}
)

@router.get("/", status_code=200)
@version(1)
async def users():
  """
  Return sample response
  """
  return [{"user_id": 1, "first_name": "Ashwin", "last_name": "Hegde", "email": "ashwin.hegde3@gmail.com"}]

@router.get("/user", status_code=200)
@version(1)
async def users():
  """
  Return sample response
  """
  return {"user_id": 1, "first_name": "Ashwin", "last_name": "Hegde", "email": "ashwin.hegde3@gmail.com"}

@router.post("/user", status_code=200)
@version(1)
async def users(user: UserModel):
  """
  Return sample response
  """
  return {"user_id": user.user_id, "first_name": user.first_name, "last_name": user.last_name, "email": user.email}
