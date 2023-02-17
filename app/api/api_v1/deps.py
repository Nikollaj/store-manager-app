import logging
from typing import Generator, Optional

from fastapi import Depends, status, HTTPException
# from jose import jwt, JWTError
from pydantic import BaseModel
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import Settings


class ApiDependencies:

    def __init__(self, settings: Settings, session_maker: sessionmaker):
        """User Auth skipped for now"""
        def get_db() -> Generator:
            db = session_maker()
            try:
                yield db
            finally:
                db.close()

        self.get_db = get_db
