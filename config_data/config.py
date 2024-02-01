from dataclasses import dataclass

from environs import Env


__all__ = ['Config', 'load_config']


@dataclass
class VkBot:
    token: str


@dataclass
class PostgresConfig:
    driver: str
    user: str
    password: str
    host: str
    port: int
    database: str


@dataclass
class RedisConfig:
    driver: str
    user: str
    password: str
    host: str
    port: int
    database: str


@dataclass
class Config:
    vk_bot: VkBot
    postgres: PostgresConfig
    redis: RedisConfig


def load_config() -> Config:
    """
    Create the bot config class.
    """

    env: Env = Env()
    env.read_env()

    return Config(vk_bot=VkBot(token=env('BOT_TOKEN')),
                  postgres=PostgresConfig(driver=env('POSTGRES_DRIVER'),
                                          user=env('POSTGRES_USER'),
                                          password=env('POSTGRES_PASSWORD'),
                                          host=env('POSTGRES_HOST'),
                                          port=int(env('POSTGRES_PORT')),
                                          database=env('POSTGRES_DB')),
                  redis=RedisConfig(driver=env('REDIS_DRIVER'),
                                    user=env('REDIS_USER'),
                                    password=env('REDIS_PASSWORD'),
                                    host=env('REDIS_HOST'),
                                    port=int(env('REDIS_PORT')),
                                    database=env('REDIS_DB')))
