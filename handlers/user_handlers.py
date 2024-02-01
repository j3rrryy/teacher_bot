from cgitb import text
from vkbottle.bot import BotLabeler, Message
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from lexicon import LEXICON_RU, ERROR_LEXICON_RU
from keyboards import menu_kb
from middlewares import AntiFloodMiddleware
from states import GameStates


user_labeler: BotLabeler = BotLabeler()
user_labeler.message_view.register_middleware(AntiFloodMiddleware)


@user_labeler.private_message(text='Начать')
async def start(message: Message):
    await message.answer(LEXICON_RU['/start'], keyboard=menu_kb().get_json())
