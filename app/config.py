"""
Holds all service level configurations
"""

from pydantic import BaseSettings

class Configs(BaseSettings):
  """
  Return the application's metadata info
  """
  title = "beaver-server"
  description = "description"
  microservice_name = "users"
  microservice_version = "v1.0.0"

  contact = {
    "name": "Ashwin Hegde",
    "url": "https://github.com/hegdeashwin",
    "email": "ashwin.hegde3@gmail.com"
  }

  def get_hostname(self):
    """
    Return machine hostname
    """
    return "127.0.0.1"

  def get_port(self):
    """
    Return application server port. This should be unique
    amoung all the microservice exist for beaver.
    """
    return 8000

  def is_debug_mode(self):
    """
    Return debug model
    """
    return True
