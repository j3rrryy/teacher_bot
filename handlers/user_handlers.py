from vkbottle.bot import BotLabeler, Message

from lexicon import LEXICON_RU, KB_LEXICON_RU, ERROR_LEXICON_RU
from middlewares import DatabaseMiddleware
from services import heads_or_tails_game, math_game
from external_services.subject_service import get_material
from keyboards import *
from database import *

user_labeler: BotLabeler = BotLabeler()
user_labeler.message_view.register_middleware(DatabaseMiddleware)


@user_labeler.private_message(text='Начать')
async def start(message: Message):
    try:
        if not (await get_user(message.from_id, message.__dict__['postgres'])):
            await create_user(message.from_id, message.__dict__['postgres'])

        await message.answer(f'Привет, {(await message.get_user()).first_name}👋' + LEXICON_RU['start'],
                             keyboard=to_menu_kb().get_json())
    except DatabaseError:
        await message.answer(ERROR_LEXICON_RU['database_error'], keyboard=to_menu_kb().get_json())


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
    try:
        profile = await get_user(message.from_id, message.__dict__['postgres'])

        rating = LEXICON_RU['rating'] + str(profile.rating) + '\n'
        registered = LEXICON_RU['registered'] + \
                     profile.registered.strftime('%d.%m.%Y')

        await message.answer(LEXICON_RU['profile'] + rating + registered)
    except DatabaseError:
        await message.answer(ERROR_LEXICON_RU['database_error'])


@user_labeler.private_message(text=KB_LEXICON_RU['info'])
async def info(message: Message):
    await message.answer(LEXICON_RU['info'])


@user_labeler.private_message(text=KB_LEXICON_RU['coin'])
@user_labeler.private_message(payload={'game_type': 0})
async def heads_or_tails(message: Message):
    await message.answer(LEXICON_RU['choose'], keyboard=heads_or_tails_kb().get_json())


@user_labeler.private_message(text=[KB_LEXICON_RU['heads'], KB_LEXICON_RU['tails']])
async def heads_or_tails_res(message: Message):
    try:
        if heads_or_tails_game(message.text)[0]:
            new_rating = (await update_rating(message.from_id, 10, message.__dict__['postgres'])).rating
            await message.answer(LEXICON_RU['win'] + str(new_rating), keyboard=play_again_kb(0).get_json())

        else:
            new_rating = (await update_rating(message.from_id, -10, message.__dict__['postgres'])).rating
            await message.answer(LEXICON_RU['lose'] + str(new_rating), keyboard=play_again_kb(0).get_json())
    except DatabaseError:
        await message.answer(ERROR_LEXICON_RU['database_error'])


@user_labeler.private_message(text=KB_LEXICON_RU['solve'])
@user_labeler.private_message(payload={'game_type': 1})
async def solve_equation(message: Message):
    eq = math_game()

    await message.answer(LEXICON_RU['solve'] + eq[0], keyboard=choose_answer(eq[1]).get_json())


@user_labeler.private_message(payload={'correct': True})
async def solve_equation_res_1(message: Message):
    try:
        new_rating = (await update_rating(message.from_id, 10, message.__dict__['postgres'])).rating
        await message.answer(LEXICON_RU['correct'] + str(new_rating), keyboard=play_again_kb(1).get_json())
    except DatabaseError:
        await message.answer(ERROR_LEXICON_RU['database_error'])


@user_labeler.private_message(payload={'correct': False})
async def solve_equation_res_2(message: Message):
    try:
        new_rating = (await update_rating(message.from_id, -10, message.__dict__['postgres'])).rating
        await message.answer(LEXICON_RU['wrong'] + str(new_rating), keyboard=play_again_kb(1).get_json())
    except DatabaseError:
        await message.answer(ERROR_LEXICON_RU['database_error'])


@user_labeler.private_message(text=KB_LEXICON_RU['lit'])
async def get_lit(message: Message):
    await message.answer(get_material('lit'))


@user_labeler.private_message(text=KB_LEXICON_RU['rus'])
async def get_rus(message: Message):
    await message.answer(get_material('rus'))


@user_labeler.private_message(text=KB_LEXICON_RU['phys'])
async def get_phys(message: Message):
    await message.answer(get_material('phys'))


@user_labeler.private_message(text=KB_LEXICON_RU['maths'])
async def get_maths(message: Message):
    await message.answer(get_material('maths'))


@user_labeler.private_message(text=KB_LEXICON_RU['chem'])
async def get_chem(message: Message):
    await message.answer(get_material('chem'))


@user_labeler.private_message(text=KB_LEXICON_RU['it'])
async def get_it(message: Message):
    await message.answer(get_material('it'))
