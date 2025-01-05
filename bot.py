import asyncio
import logging

from vkbottle.bot import Bot, BotLabeler

from src.config import load_config
from src.handlers import user_labeler

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        force=True,
    )
    logger.info("Starting bot")

    config = load_config()
    labeler = BotLabeler()
    labeler.load(user_labeler)

    bot = Bot(token=config.bot.token, labeler=labeler)
    await bot.run_polling()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logger.exception(e)
