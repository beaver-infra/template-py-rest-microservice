"""
Holds functions used by health API
"""

from fastapi import APIRouter, status, Depends
from fastapi_versioning import version

router = APIRouter()

async def get_session():
  """
  Return a mock boolean response
  """
  return True

@router.get("/health", status_code=status.HTTP_200_OK)
@version(1)
async def is_api_online(session: bool = Depends(get_session)):
  """
  Return the session response to confirm API is up and running
  """
  return session
