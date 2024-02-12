"""
Defines endpoints for retrieving microservice information.
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
    Retrieve metadata information for the microservice.

    Parameters:
    - metadata (Metadata): Metadata object containing service information.

    Returns:
    - dict: Metadata information for the microservice.
    """
    return metadata.get_metadata()
