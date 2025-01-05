from vkbottle import BaseMiddleware
from vkbottle.bot import Message

from src.database import get_sessionmaker


class DatabaseMiddleware(BaseMiddleware[Message]):
    def __init__(self, event, view):
        super().__init__(event, view)
        self.postgres = get_sessionmaker()

    async def pre(self):
        self.event.__dict__["postgres"] = self.postgres
