from datetime import date

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.errors import DatabaseError

from .models import User


async def create_user(
    user_id: int, sessionmaker: async_sessionmaker[AsyncSession]
) -> None:
    """
    Create user in the db
    """

    async with sessionmaker() as session:
        async with session.begin():
            try:
                user = User(user_id=user_id)
                session.add(user)
            except Exception as e:
                await session.rollback()
                raise DatabaseError from e


async def get_user(
    user_id: int, sessionmaker: async_sessionmaker[AsyncSession]
) -> dict[str, int | date]:
    """
    Get user from the db
    """

    async with sessionmaker() as session:
        async with session.begin():
            try:
                user = await session.get(User, user_id)
                return user.columns_to_dict()
            except Exception as e:
                await session.rollback()
                raise DatabaseError from e


async def update_rating(
    user_id: int, add_rating: int, sessionmaker: async_sessionmaker[AsyncSession]
) -> dict[str, int | date]:
    """
    Update user rating in the db
    """

    async with sessionmaker() as session:
        async with session.begin():
            try:
                user = await session.get(User, user_id)
                if user.rating < abs(add_rating) and add_rating < 0:
                    user.rating = 0
                else:
                    user.rating += add_rating
                return user.columns_to_dict()
            except Exception as e:
                await session.rollback()
                raise DatabaseError from e


async def get_top(user_id: int, sessionmaker: async_sessionmaker[AsyncSession]) -> int:
    """
    Get user rating position
    """

    async with sessionmaker() as session:
        async with session.begin():
            try:
                user_rating = (await session.get(User, user_id)).rating
                higher_ratings = (
                    await session.execute(
                        select(func.count()).where(User.rating > user_rating)
                    )
                ).scalar()
                user_pos = higher_ratings + 1
                return user_pos
            except Exception as e:
                await session.rollback()
                raise DatabaseError from e
