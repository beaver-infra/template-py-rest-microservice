"""
Holds all common handler functions used within services
"""
import os
from functools import lru_cache

from app.configs import development, production, stage
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
def get_instance_type_configs():
    """
    Return system instance type where the service is running, either dev/stage/production env,
    depends on system variable BEAVER_API_SYS_INS_TYPE configured
    """
    sys_ins_type = os.getenv("BEAVER_API_SYS_INS_TYPE")

    if sys_ins_type == "PRODUCTION":
        return production

    if sys_ins_type == "STAGE":
        return stage

    if sys_ins_type == None or sys_ins_type == "DEVELOPMENT":
        return development


def get_app_port():
    """
    Return service port on which its running
    """
