"""
Holds service initialization
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi_versioning import VersionedFastAPI
from app.api import api_router
# from app.config import Configs

# configs = Configs()

# Create FastAPI app instance and return with default configured settings
app = FastAPI(
  # metadata
  # debug=configs.is_debug_mode()
)

# Allow cross origin resource sharing with default configurations
# Refer https://fastapi.tiangolo.com/tutorial/cors/
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

# Compress response for any request that includes gzip in the accept-encoding header
# Refer https://fastapi.tiangolo.com/advanced/middleware/#gzipmiddleware
app.add_middleware(GZipMiddleware)

# Reference to all the microservice routes including special routes like info and health
app.include_router(api_router)

# Configure API versioning by setting prefix format for all APIs
app = VersionedFastAPI(app, version_format="{major}", prefix_format="/api/v{major}")

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
