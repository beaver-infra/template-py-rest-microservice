"""
Defines the data model and schema for handling user-related requests and responses.
"""

from dataclasses import dataclass
from typing import Optional

from pydantic import BaseModel, Field


@dataclass
class UserModel(BaseModel):
    """
    Represents the structure of user data.
    """

    user_id: Optional[int] = None  # Unique identifier for the user, if available
    first_name: str = Field(
        None, title="First name", max_length=50
    )  # User's first name
    last_name: str = Field(None, title="Last name", max_length=50)  # User's last name
    email: Optional[str] = None  # User's email address
