"""
Holds all common handler functions used within services
"""
import os
from functools import lru_cache

from omegaconf import OmegaConf

from app.metadata import Metadata


@lru_cache()
def get_service_metadata():
    """
    Return Configs class which holds application's metadata info
    @lru_cache() Decorates to return the same value that was returned the first time,
    instead of computing it again, executing the code of the function every time.
    """
    return Metadata()


@lru_cache()
def load_config():
    """
    Return system instance type where the service is running, either dev/stage/production env,
    depends on system variable INSTANCE_ENVIRONMENT configured
    """
    instance_environment = os.getenv("INSTANCE_ENVIRONMENT")
    file = OmegaConf.load("app/configs/development.yml")
    
    if instance_environment == "PRODUCTION":
        file = OmegaConf.load("app/configs/production.yml")

    if instance_environment == "STAGE":
        file = OmegaConf.load("app/configs/stage.yml")

    return file
