from pydantic import BaseSettings
import os
from typing import Optional


class Settings(BaseSettings):

    SQLALCHEMY_DATABASE_URI: Optional[str] = \
        "postgresql+psycopg2://postgres:postgres@localhost:5432/storage"

    API_V1_STR: str = os.getenv("API_PATH_V1", "/api/v1")

    HDD_KEYS = ["name", "manufacturer", "total", "allocated", "capacity_gb", "size", "rpm"]
    SSD_KEYS = ["name", "manufacturer", "total", "allocated", "capacity_gb", "interface"]
    CPU_KEYS = ["name", "manufacturer", "total", "allocated", "cores", "socket", "power_watts"]

