from vkbottle import Keyboard, KeyboardButtonColor, Text

from lexicon import KB_LEXICON_RU


def menu_kb() -> Keyboard:
    kb = (
        Keyboard(inline=True)
        .add(Text(KB_LEXICON_RU['subjects']),
             color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text(KB_LEXICON_RU['games']),
             color=KeyboardButtonColor.SECONDARY)
        .row()
        .add(Text(KB_LEXICON_RU['profile']), color=KeyboardButtonColor.PRIMARY)
    )

    return kb


def subjects_kb() -> Keyboard:
    ...
