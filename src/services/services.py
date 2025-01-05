import random


def heads_or_tails_game(user_pred: str) -> tuple[bool, str]:
    ch = random.choice(["Орел", "Решка"])
    return ch == user_pred, ch


def math_game() -> tuple[str, int]:
    OPERATIONS = "+-*/"

    num_1 = random.randint(-50, 50)
    num_2 = random.randint(-50, 50)
    num_3 = random.randint(-50, 50)

    res = (
        str(num_1)
        + f" {random.choice(OPERATIONS)} "
        + ("(" + str(num_2) + ")" if num_2 < 0 else str(num_2))
        + f" {random.choice(OPERATIONS)} "
        + ("(" + str(num_3) + ")" if num_3 < 0 else str(num_3))
    )
    return res, int(eval(res))
