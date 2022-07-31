from fastapi import APIRouter
from fastapi_versioning import version

router = APIRouter()

from services.users import ProfileModel

@router.get("/user", status_code=200)
@version(1)
async def users():
  p = ProfileModel()
  return p.helloWorld()
