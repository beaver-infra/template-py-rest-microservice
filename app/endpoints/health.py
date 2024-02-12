"""
This module contains functions used by the health API.
"""

from fastapi import APIRouter, Depends, status
from fastapi_versioning import version

router = APIRouter()


async def get_session():
    """
    Returns a mock boolean response indicating whether the session is active.

    Returns:
        bool: True if the session is active, otherwise False.
    """
    return True


@router.get("/health", status_code=status.HTTP_200_OK)
@version(1)
async def is_api_online(session: bool = Depends(get_session)):
    """
    Returns the session response to confirm that the API is up and running.

    Args:
        session (bool): A boolean value indicating the session status.

    Returns:
        bool: The session status, True if the API is online, otherwise False.
    """
    return session
