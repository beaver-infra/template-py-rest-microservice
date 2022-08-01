from config import Settings
# from functools import lru_cache

# @lru_cache()
def get_settings():
  """
  Return Settings class which holds application's metadata info
  """
  return Settings()