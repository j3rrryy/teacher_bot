from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from database import User
from errors import DatabaseError


async def create_user(user_id: int, sessionmaker: async_sessionmaker[AsyncSession]) -> None:
    '''
    Create user in the db
    '''

    async with sessionmaker() as session:
        async with session.begin():
            try:
                user = User(user_id=user_id)
                session.add(user)
            except:
                await session.rollback()
                raise DatabaseError


async def get_user(user_id: int, sessionmaker: async_sessionmaker[AsyncSession]) -> User:
    '''
    Get user from the db
    '''

    async with sessionmaker() as session:
        async with session.begin():
            try:
                user = await session.get(User, user_id)
                return user
            except:
                await session.rollback()
                raise DatabaseError


async def update_rating(user_id: int, add_rating: int, sessionmaker: async_sessionmaker[AsyncSession]) -> User:
    '''
    Update user rating in the db
    '''

    async with sessionmaker() as session:
        async with session.begin():
            try:
                user = await session.get(User, user_id)
                if user.rating < abs(add_rating) and add_rating < 0:
                    user.rating = 0
                else:
                    user.rating += add_rating
                return user
            except:
                await session.rollback()
                raise DatabaseError
