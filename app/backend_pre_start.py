import logging
import os
from app.core.config import Settings
from app.db.session import create_session_maker


def init() -> None:
    settings = Settings()
    session_maker = create_session_maker(settings)
    with session_maker() as db:
        try:
            # Try to create session to check if DB is awake
            db.execute("SELECT 1")
        except Exception as e:
            print(e)
            raise e


def main() -> None:
    print("Initializing service")
    init()
    print("Service finished initializing")


if __name__ == "__main__":
    main()
