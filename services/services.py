from random import choice, randint


def heads_or_tails_game(user_pred: str) -> tuple[bool, str]:
    ch = choice(['Орел', 'Решка'])
    return ch == user_pred, ch


def math_game() -> tuple[str, int]:
    ops = '+-*/'

    res = str(randint(-50, 50)) + choice(ops) + str(randint(-50, 50)) + \
        choice(ops) + str(randint(-50, 50))  # fix -- with negativ nums

    return res, int(eval(res))
