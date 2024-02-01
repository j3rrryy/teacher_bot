import asyncio
import logging

from vkbottle.bot import Bot, BotLabeler

from config_data import load_config, Config
from handlers import user_labeler


logger = logging.getLogger(__name__)


async def main() -> None:

    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')

    config: Config = load_config()

    labeler: BotLabeler = BotLabeler()
    labeler.load(user_labeler)

    bot: Bot = Bot(token=config.vk_bot.token, labeler=labeler)

    await bot.run_polling()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as e:
        logger.error('Bot stopped!')
        print(e)
