from ast import Call
from typing import Callable
from fastapi import FastAPI

def _startup_model(app: FastAPI) -> None:
  pass

def _shutdown_model(app: FastAPI) -> None:
  pass

def start_app_handler(app: FastAPI) -> Callable:
  def startup() -> None:
    _startup_model(app)
  return startup

def shutdown_app_handler(app: FastAPI) -> Callable:
  def shutdown() -> None:
    _shutdown_model(app)
  return shutdown
