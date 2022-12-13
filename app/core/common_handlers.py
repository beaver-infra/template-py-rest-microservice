"""
Holds all common handler functions used within services
"""
import os
from functools import lru_cache
from app.metadata import Metadata
from app.configs import development, production, stage

@lru_cache()
def get_service_metadata():
  """
  Return Configs class which holds application's metadata info
  @lru_cache() Decorates to return the same value that was returned the first time,
  instead of computing it again, executing the code of the function every time.
  """
  return Metadata()

def get_system_env():
  """
  Return Configs ckass
  """
  api_sys_env = os.getenv("BEAVER_API_SYS_INS_TYPE", "DEVELOPMENT")

  if api_sys_env == "PRODUCTION":
    return production

  if api_sys_env == "STAGE":
    return stage

  if api_sys_env == None or api_sys_env == "DEVELOPMENT":
    return development
