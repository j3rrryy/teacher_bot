from vkbottle.bot import BotLabeler, Message
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from lexicon import LEXICON_RU, KB_LEXICON_RU, ERROR_LEXICON_RU
from middlewares import DatabaseMiddleware
from states import GameStates
from services import heads_or_tails_game
from keyboards import *


user_labeler: BotLabeler = BotLabeler()
user_labeler.message_view.register_middleware(DatabaseMiddleware)


@user_labeler.private_message(text='Начать')
async def start(message: Message):
    await message.answer(LEXICON_RU['start'], keyboard=to_menu_kb().get_json())


@user_labeler.private_message(text=KB_LEXICON_RU['menu'])
async def menu(message: Message):
    await message.answer(LEXICON_RU['menu'], keyboard=menu_kb().get_json())


@user_labeler.private_message(text=KB_LEXICON_RU['subjects'])
async def subjects(message: Message):
    await message.answer(LEXICON_RU['subjects'], keyboard=subjects_kb().get_json())


@user_labeler.private_message(text=KB_LEXICON_RU['games'])
async def games(message: Message):
    await message.answer(LEXICON_RU['games'], keyboard=games_kb().get_json())


@user_labeler.private_message(text=KB_LEXICON_RU['profile'])
async def profile(message: Message):
    await message.answer(LEXICON_RU['profile'])


@user_labeler.private_message(text=KB_LEXICON_RU['coin'])
@user_labeler.private_message(payload={'game_type': 0})
async def coin(message: Message):
    await message.answer(LEXICON_RU['choose'], keyboard=heads_or_tails_kb().get_json())


@user_labeler.private_message(text=[KB_LEXICON_RU['heads'], KB_LEXICON_RU['tails']])
async def heads_or_tails_res(message: Message):
    if heads_or_tails_game(message.text)[0]:
        await message.answer(LEXICON_RU['win'], keyboard=play_again_kb().get_json())
    else:
        await message.answer(LEXICON_RU['lose'], keyboard=play_again_kb().get_json())
