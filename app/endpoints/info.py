"""
Holds functions used by info API
"""

from fastapi import APIRouter, Depends, status
from fastapi_versioning import version

from app.core.common_handlers import get_service_metadata
from app.metadata import Metadata

router = APIRouter()


@router.get("/info", status_code=status.HTTP_200_OK)
@version(1)
async def info(metadata: Metadata = Depends(get_service_metadata)):
    """
    Return microservice metadata info
    """
    return metadata.get_metadata()
