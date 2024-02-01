from redis.asyncio import Redis, from_url
from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from config_data import Config, load_config


def get_postgres_sessionmaker() -> async_sessionmaker[AsyncSession]:
    '''
    Configure the postgres connection
    '''

    config: Config = load_config()

    postgres_url = URL.create(
        drivername=config.postgres.driver,
        username=config.postgres.user,
        password=config.postgres.password,
        host=config.postgres.host,
        port=config.postgres.port,
        database=config.postgres.database
    )

    async_engine = create_async_engine(url=postgres_url, pool_pre_ping=True)
    session_maker = async_sessionmaker(bind=async_engine, class_=AsyncSession)

    return session_maker


def get_redis_client() -> Redis:
    '''
    Configure the redis connection
    '''

    config: Config = load_config()

    redis = from_url(
        f'{config.redis.driver}://{config.redis.user}:{config.redis.password}@{config.redis.host}:{config.redis.port}/{config.redis.database}',
        encoding='utf8',
        decode_responses=True
    )

    return redis
