"""
Contains common handler functions utilized across services.
"""

import os
from functools import lru_cache

from omegaconf import OmegaConf

from app.metadata import Metadata


@lru_cache()
def get_service_metadata():
    """
    Retrieves the Configs class containing the application's metadata information.

    Returns:
        Metadata: An instance of the Metadata class.

    Notes:
        - `@lru_cache()` decorator is used to cache the result of this function,
          avoiding recomputation upon subsequent calls.
    """
    return Metadata()


@lru_cache()
def load_config():
    """
    Loads the configuration based on the system instance type where the service is running.

    Returns:
        OmegaConf.DictConfig: The loaded configuration file.

    Notes:
        - The environment is determined by the system variable `INSTANCE_ENVIRONMENT`.
        - Configuration files are loaded based on the instance environment:
          - For `PRODUCTION`: production.yml
          - For `STAGE`: stage.yml
          - For any other value or unset variable: development.yml is loaded.
    """
    instance_environment = os.getenv("INSTANCE_ENVIRONMENT")
    file = OmegaConf.load("app/configs/development.yml")

    if instance_environment == "PRODUCTION":
        file = OmegaConf.load("app/configs/production.yml")

    if instance_environment == "STAGE":
        file = OmegaConf.load("app/configs/stage.yml")

    return file
