from redis.asyncio import Redis
from vkbottle import BaseMiddleware
from vkbottle.bot import Message
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from database import get_postgres_sessionmaker, get_redis_client


class DatabaseMiddleware(BaseMiddleware[Message]):
    '''
    Pass db to handlers
    '''

    def __init__(self, event, view):
        super().__init__(event, view)
        self.postgres: async_sessionmaker[AsyncSession] = get_postgres_sessionmaker(
        )
        self.redis: Redis = get_redis_client()

    async def pre(self):
        ...
