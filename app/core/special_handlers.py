"""
Defines special handler functions utilized within services.
"""

# Disabling pylint to suppress linting warnings
# pylint: disable-all

from typing import Callable
from fastapi import FastAPI


def _startup_event(app: FastAPI) -> None:
    """
    Execute before the application starts.

    This function ensures that the application does not start
    receiving requests until all startup event handlers have completed.
    """
    pass


def _shutdown_event(app: FastAPI) -> None:
    """
    Execute before the application starts.

    This function ensures that the application does not start
    receiving requests until all shutdown event handlers have completed.
    """
    pass


def startup_event_handler(app: FastAPI) -> Callable:
    """
    Wrap function to handle startup events.
    """

    def startup() -> None:
        _startup_event(app)

    return startup


def shutdown_event_handler(app: FastAPI) -> Callable:
    """
    Wrap function to handle shutdown events.
    """

    def shutdown() -> None:
        _shutdown_event(app)

    return shutdown
