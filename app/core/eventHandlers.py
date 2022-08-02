from typing import Callable
from fastapi import FastAPI

def _startup_model(app: FastAPI) -> None:
  pass

def _shutdown_model(app: FastAPI) -> None:
  pass

def start_app_handler(app: FastAPI) -> Callable:
  """
  Startup event handler
  """
  def startup() -> None:
    _startup_model(app)
  return startup

def shutdown_app_handler(app: FastAPI) -> Callable:
  """
  Shutdown event handler
  """
  def shutdown() -> None:
    _shutdown_model(app)
  return shutdown
