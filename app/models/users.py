"""
Holds the model class for request and response for Users sample routes
"""

from pydantic import BaseModel, Field
from typing import Optional

class UserModel(BaseModel):
  """
  User model
  """
  user_id: Optional[int] = None
  first_name: str = Field(
    None, title="First name", max_length=50
  )
  last_name: str = Field(
    None, title="Last name", max_length=50
  )
  email: str
