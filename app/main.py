from app.core.config import Settings
from fastapi import FastAPI
from app.web_components import WebComponents
from app.models.resources.storage.storage import Storage

app = FastAPI(title="StoreManagerApp")
settings = Settings()
components = WebComponents(settings)
app.include_router(components.api.router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
