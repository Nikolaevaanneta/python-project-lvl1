import random
from typing import Tuple


def assignment():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def make_question_with_answer() -> Tuple[str, str]:
    question = random.randrange(1, 100)
    answer = 'no' if question % 2 else 'yes'
    return str(question), answer


def is_prime(num: int):
    if num < 2:
        return False
    if num == 2:
        return True
    if num > 2 and not num % 2:
        return False

    div = 3
    while div <= num // 2:
        if not num % div:
            return False
        div += 2
    return True
