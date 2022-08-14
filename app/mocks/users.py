"""
Holds functions to return API mock response
"""

async def mock_users():
  """
  Return mock response for users API
  """
  return [{
    "user_id": 1,
    "first_name": "Ashwin",
    "last_name": "Hegde",
    "email": "ashwin.hegde3@gmail.com"
  }]
