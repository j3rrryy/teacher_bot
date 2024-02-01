from random import choice


def heads_or_tails_game(user_pred: str) -> tuple[bool, str]:
    ch = choice(['Орел', 'Решка'])
    return ch == user_pred, ch
