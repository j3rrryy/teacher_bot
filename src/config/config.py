from dataclasses import dataclass

from environs import Env

__all__ = ["Config", "load_config"]


@dataclass(slots=True)
class Bot:
    token: str


@dataclass(slots=True)
class PostgresConfig:
    driver: str
    user: str
    password: str
    host: str
    port: int
    database: str


@dataclass(slots=True)
class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    bot: Bot
    postgres: PostgresConfig


def load_config():
    env: Env = Env()
    env.read_env()

    return Config(
        bot=Bot(token=env("BOT_TOKEN")),
        postgres=PostgresConfig(
            driver=env("POSTGRES_DRIVER"),
            user=env("POSTGRES_USER"),
            password=env("POSTGRES_PASSWORD"),
            host=env("POSTGRES_HOST"),
            port=int(env("POSTGRES_PORT")),
            database=env("POSTGRES_DB"),
        ),
    )
