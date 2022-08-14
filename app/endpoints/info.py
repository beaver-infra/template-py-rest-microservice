"""
Holds functions used by info API
"""

from fastapi import APIRouter, Depends, status
from fastapi_versioning import version
from app.core.common_handlers import get_configs
from app.config import Configs

router = APIRouter()

@router.get("/info", status_code=status.HTTP_200_OK)
@version(1)
async def info(config: Configs = Depends(get_configs)):
  """
  Return microservice metadata info
  """
  return {
    "microservice_name": config.microservice_name,
    "microservice_version": config.microservice_version,
    "contact": config.contact
  }
