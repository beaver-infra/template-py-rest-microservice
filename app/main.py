"""
Holds service initialization
"""

import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi_versioning import VersionedFastAPI
from app.routers.router import api_router
from app.config import Settings

# Setup logger configuration
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

# Get root logger. The __name__ resolve to "main" since we are at the root of the project.
# This will get the root logger since no logger in the configuration has this name.
logger = logging.getLogger(__name__)

def get_app() -> FastAPI:
  """
  Create FastAPI app instance and return with default configured settings
  """
  setting = Settings()
  fast_app = FastAPI(
    title=setting.title,
    description=setting.description,
    contact=setting.contact,
    debug=setting.is_debug_mode(),
  )

  # Allow cross origin resource sharing with default configurations
  # Refer https://fastapi.tiangolo.com/tutorial/cors/
  fast_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
  )

  # Compress response for any request that includes gzip in the accept-encoding header
  # Refer https://fastapi.tiangolo.com/advanced/middleware/#gzipmiddleware
  fast_app.add_middleware(GZipMiddleware)

  # Reference to all the microservice routes including special routes like info and health
  fast_app.include_router(api_router)

  # Configure API versioning by setting prefix format for all APIs
  fast_app = VersionedFastAPI(fast_app, version_format="{major}", prefix_format="/api/v{major}")

  # Configure common event handlers for service startup and shutdown to handler special use cases
  # fast_app.add_event_handler("startup", start_app_handler(fast_app))
  # fast_app.add_event_handler("shutdown", shutdown_app_handler(fast_app))

  return fast_app

app = get_app()

# A function that should be run before the application starts.
# Your application won't start receiving requests
# until all the startup event handlers have completed.
# Enable below code if required
# @app.on_event("startup")
# async def startup_event():
#   pass

# A function that should be run when the application is shutting down.
# Enable below code if required
# @app.on_event("shutdown")
# async def shutdown_event():
#   pass
