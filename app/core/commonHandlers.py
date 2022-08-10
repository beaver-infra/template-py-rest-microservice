from app.config import Settings
from functools import lru_cache

@lru_cache()
def get_settings():
  """
  Return Settings class which holds application's metadata info
  @lru_cache() Decorates to return the same value that was returned the first time,
  instead of computing it again, executing the code of the function every time.
  """
  return Settings()
