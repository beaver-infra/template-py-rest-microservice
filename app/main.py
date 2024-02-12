"""
Import necessary modules and packages
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi_versioning import VersionedFastAPI

from app.api import api_router
from app.core.special_handlers import (shutdown_event_handler,
                                       startup_event_handler)
from app.metadata import Metadata

# Initialize metadata object
metadata = Metadata()


def get_app() -> FastAPI:
    """
    Create and configure a FastAPI app instance with default settings.

    Returns:
        FastAPI: A configured FastAPI app instance.
    """
    # Create FastAPI instance with metadata details
    fast_app = FastAPI(
        title=metadata.get_service_title(),
        description=metadata.get_service_description(),
        version=metadata.get_service_release_version(),
        contact=metadata.get_service_contact(),
        # debug=metadata.is_debug_mode()
    )

    # Allow Cross-Origin Resource Sharing (CORS) with default configurations
    # Reference: https://fastapi.tiangolo.com/tutorial/cors/
    fast_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Compress response for any request that includes gzip in the accept-encoding header
    # Reference: https://fastapi.tiangolo.com/advanced/middleware/#gzipmiddleware
    fast_app.add_middleware(GZipMiddleware)

    # Include all microservice routes including special routes like info and health
    fast_app.include_router(api_router)

    # Configure API versioning by setting prefix format for all APIs
    fast_app = VersionedFastAPI(
        fast_app, version_format="{major}", prefix_format="/api/v{major}"
    )

    # Configure startup and shutdown event handlers
    fast_app.add_event_handler("startup", startup_event_handler(fast_app))
    fast_app.add_event_handler("shutdown", shutdown_event_handler(fast_app))

    return fast_app


# Initialize the FastAPI app
app = get_app()
