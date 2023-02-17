from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import Settings


def create_session_maker(settings: Settings) -> sessionmaker:
    engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)

