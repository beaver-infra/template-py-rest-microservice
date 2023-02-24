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
    depends on system variable BEAVER_API_SYS_INS_TYPE configured
    """
    sys_ins_type = os.getenv("BEAVER_API_SYS_INS_TYPE")

    if sys_ins_type in "PRODUCTION":
        file = OmegaConf.load("app/configs/production.yml")

    if sys_ins_type in "STAGE":
        file = OmegaConf.load("app/configs/stage.yml")

    if sys_ins_type in "DEVELOPMENT":
        file = OmegaConf.load("app/configs/development.yml")

    return file
