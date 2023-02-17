from app.core.config import Settings
from app.api.api_v1.components import APIComponents
from app.db.session import create_session_maker


class WebComponents:
    def __init__(self, settings: Settings):
        self.session_maker = create_session_maker(settings)
        self.api = APIComponents(settings, self.session_maker)

