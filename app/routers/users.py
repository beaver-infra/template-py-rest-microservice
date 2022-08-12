"""
Holds functions used by Users Sample API
"""

from fastapi import APIRouter
from fastapi_versioning import version
from app.services.users import ProfileModel

router = APIRouter()

@router.get("/user", status_code=200)
@version(1)
async def users():
  """
  Return response model of users services as an example
  """
  profile_model = ProfileModel()
  return profile_model.hello_world()
