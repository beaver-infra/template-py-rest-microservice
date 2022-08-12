"""
Holds the model class for request and response for Users sample routes
"""

import dataclasses

@dataclasses.dataclass
class ProfileModel():
  """
  Profile model
  """
  def hello_world(self):
    """
    hello world implementation
    """
    response = {}
    response["status"] = "SUCCESS"
    response["data"] = str({
      "text": "Hello World!"
    })
    return response
