import uvicorn
from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI
from api.routers.router import api_router
from core.eventHandlers import (start_app_handler, shutdown_app_handler)

def get_app() -> FastAPI:
  fast_app = FastAPI(
    debug=True
  )
  fast_app.include_router(api_router)
  fast_app = VersionedFastAPI(fast_app, version_format="{major}", prefix_format="/v{major}")
  fast_app.add_event_handler("startup", start_app_handler(fast_app))
  fast_app.add_event_handler("shutdown", shutdown_app_handler(fast_app))
  return fast_app

app = get_app()

if __name__ == "__main__":
  try:
    uvicorn.run(
      "main:app",
      host="0.0.0.0",
      port=4000
    )
  except Exception as e:
    print(e)
