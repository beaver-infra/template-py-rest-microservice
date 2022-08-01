from fastapi import APIRouter
from fastapi_versioning import version
from services.users import ProfileModel

router = APIRouter()

@router.get("/user", status_code=200)
@version(1)
async def users():
  """
  Return response model of users services as an example
  """
  p = ProfileModel()
  return p.helloWorld()
