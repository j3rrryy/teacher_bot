from random import shuffle, randint

from vkbottle import Keyboard, KeyboardButtonColor, Text

from lexicon import KB_LEXICON_RU


def to_menu_kb() -> Keyboard:
    kb = (
        Keyboard()
        .add(Text(KB_LEXICON_RU['menu']),
             color=KeyboardButtonColor.POSITIVE)
    )

    return kb


def menu_kb() -> Keyboard:
    kb = (
        Keyboard(inline=True)
        .add(Text(KB_LEXICON_RU['subjects']),
             color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text(KB_LEXICON_RU['games']),
             color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text(KB_LEXICON_RU['profile']),
             color=KeyboardButtonColor.PRIMARY)
    )

    return kb


def subjects_kb() -> Keyboard:
    kb = (
        Keyboard(inline=True)
        .add(Text(KB_LEXICON_RU['rus']),
             color=KeyboardButtonColor.SECONDARY)
        .add(Text(KB_LEXICON_RU['maths']),
             color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text(KB_LEXICON_RU['lit']),
             color=KeyboardButtonColor.SECONDARY)
        .add(Text(KB_LEXICON_RU['it']),
             color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text(KB_LEXICON_RU['chem']),
             color=KeyboardButtonColor.SECONDARY)
        .add(Text(KB_LEXICON_RU['phys']),
             color=KeyboardButtonColor.SECONDARY)
    )

    return kb


def games_kb() -> Keyboard:
    kb = (
        Keyboard(inline=True)
        .add(Text(KB_LEXICON_RU['solve']),
             color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text(KB_LEXICON_RU['coin']),
             color=KeyboardButtonColor.SECONDARY)
    )

    return kb


def heads_or_tails_kb() -> Keyboard:
    kb = (
        Keyboard(inline=True)
        .add(Text(KB_LEXICON_RU['heads']),
             color=KeyboardButtonColor.POSITIVE)
        .add(Text(KB_LEXICON_RU['tails']),
             color=KeyboardButtonColor.NEGATIVE)
    )

    return kb


def choose_answer(correct: int) -> Keyboard:
    answrs = [correct,
              randint(correct - 50, correct + 50),
              randint(correct - 50, correct + 50),
              randint(correct - 50, correct + 50)]
    shuffle(answrs)

    kb = (
        Keyboard(inline=True)
        .add(Text(str(answrs[0]), payload={'correct': correct == answrs[0]}),
             color=KeyboardButtonColor.SECONDARY)
        .add(Text(str(answrs[1]), payload={'correct': correct == answrs[0]}),
             color=KeyboardButtonColor.SECONDARY)
        .add(Text(str(answrs[2]), payload={'correct': correct == answrs[0]}),
             color=KeyboardButtonColor.SECONDARY)
        .add(Text(str(answrs[3]), payload={'correct': correct == answrs[0]}),
             color=KeyboardButtonColor.SECONDARY)
    )

    return kb


def play_again_kb(game_type: int) -> Keyboard:
    kb = (
        Keyboard(inline=True)
        .add(Text(KB_LEXICON_RU['play_again'], payload={'game_type': game_type}),
             color=KeyboardButtonColor.POSITIVE)
    )

    return kb
