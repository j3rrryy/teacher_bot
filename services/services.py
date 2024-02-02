from random import choice, randint


def heads_or_tails_game(user_pred: str) -> tuple[bool, str]:
    ch = choice(['Орел', 'Решка'])
    return ch == user_pred, ch


def math_game() -> tuple[str, int]:
    ops = '+-*/'

    num_1 = randint(-50, 50)
    num_2 = randint(-50, 50)
    num_3 = randint(-50, 50)

    res = str(num_1) + choice(ops) \
        + ('(' + str(num_2) + ')' if num_1 < 0 else str(num_2)) + choice(ops) \
        + ('(' + str(num_3) + ')' if num_1 < 0 else str(num_3))

    return res, int(eval(res))
