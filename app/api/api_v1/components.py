from app.core.config import Settings
from fastapi import APIRouter
from app.api.api_v1.endpoints.storage_manipulation import StorageRoutes
from sqlalchemy.orm import sessionmaker
from app.api.api_v1.deps import ApiDependencies


class APIComponents:
    def __init__(self, settings: Settings, session_maker: sessionmaker):
        self.api_dependencies = ApiDependencies(settings, session_maker)

        self.router = APIRouter()
        self.storage_routes = StorageRoutes(api_dependencies=self.api_dependencies)
        self.router.include_router(self.storage_routes.router, prefix="/manage",
                                   tags=["Manage Storage Route"])

