"""
Holds all common handler functions used within services
"""

from functools import lru_cache
from app.config import Configs

@lru_cache()
def get_configs():
  """
  Return Configs class which holds application's metadata info
  @lru_cache() Decorates to return the same value that was returned the first time,
  instead of computing it again, executing the code of the function every time.
  """
  return Configs()
