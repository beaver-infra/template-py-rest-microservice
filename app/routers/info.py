from fastapi import APIRouter, Depends, status
from fastapi_versioning import version
from app.core.commonHandlers import get_settings
from app.config import Settings

router = APIRouter()

@router.get("/info", status_code=status.HTTP_200_OK)
@version(1)
async def info(settings: Settings = Depends(get_settings)):
  """
  Return microservice metadata info
  """
  return {
    "microservice_name": settings.microservice_name,
    "microservice_version": settings.microservice_version,
    "contact": settings.contact
  }
