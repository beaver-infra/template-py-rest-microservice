from pydantic import BaseSettings

class Settings(BaseSettings):
  """
  Return the application's metadata info
  """
  app_name: str = "Beaver Server"
  microservice_name: str = "users"

  def get_hostname():
    """
    Return machine hostname
    """
    return "127.0.0.1"

  def get_port():
    """
    Return application server port. This should be unique amoung all the microservice exist for beaver.
    """
    return 8000
