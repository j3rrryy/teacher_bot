from vkbottle import BaseMiddleware
from vkbottle.bot import Message
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from database import get_postgres_sessionmaker


class DatabaseMiddleware(BaseMiddleware[Message]):
    '''
    Pass db to handlers
    '''

    def __init__(self, event, view):
        super().__init__(event, view)
        self.postgres: async_sessionmaker[AsyncSession] = get_postgres_sessionmaker(
        )

    async def pre(self):
        self.event.__dict__['postgres'] = self.postgres
