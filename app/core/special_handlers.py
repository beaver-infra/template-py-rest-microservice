"""
Holds all special handler functions used within services
"""
# pylint: disable-all
from typing import Callable

from fastapi import FastAPI

def _startup_event(app: FastAPI) -> None:
    """
    A function that should be run before the application starts.
    Your application won't start receiving requests
    until all the startup event handlers have completed.
    """
    pass


def _shutdown_event(app: FastAPI) -> None:
    """
    A function that should be run before the application starts.
    Your application won't start receiving requests
    until all the startup event handlers have completed.
    """
    pass


def startup_event_handler(app: FastAPI) -> Callable:
    """
    A startup event handler wrapper function
    """

    def startup() -> None:
        _startup_event(app)

    return startup


def shutdown_event_handler(app: FastAPI) -> Callable:
    """
    A shutdown event handler wrapper function
    """

    def shutdown() -> None:
        _shutdown_event(app)

    return shutdown
