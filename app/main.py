import uvicorn
from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from routers.router import api_router
from core.eventHandlers import (start_app_handler, shutdown_app_handler)
from config import Settings

def get_app() -> FastAPI:
  """
  Create FastAPI app instance and return with default configured settings
  debug=True is set for dev and stage env whereas debug=False is set for production env
  """
  debugMode = True
  fast_app = FastAPI(
    debug=debugMode
  )

  """
  Allow cross origin resource sharing with default configurations
  Refer https://fastapi.tiangolo.com/tutorial/cors/ 
  """
  fast_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
  )
  
  """
  Compress response for any request that includes gzip in the accept-encoding header
  Refer https://fastapi.tiangolo.com/advanced/middleware/#gzipmiddleware
  """
  fast_app.add_middleware(GZipMiddleware)

  """
  Reference to all the microservice routes including special routes like info and health
  """
  fast_app.include_router(api_router)
  
  """
  Configure API versioning by setting prefix format for all APIs
  """
  fast_app = VersionedFastAPI(fast_app, version_format="{major}", prefix_format="/api/v{major}")

  """
  Configure common event handlers for service startup and shutdown to handler special use cases
  """
  fast_app.add_event_handler("startup", start_app_handler(fast_app))
  fast_app.add_event_handler("shutdown", shutdown_app_handler(fast_app))

  return fast_app

app = get_app()

if __name__ == "__main__":
  try:
    settings = Settings()
    uvicorn.run(
      "main:app",
      host=settings.get_hostname(),
      port=settings.get_port(),
      reload=True
    )
  except Exception as e:
    print(e)
