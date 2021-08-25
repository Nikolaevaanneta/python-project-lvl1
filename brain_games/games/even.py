import random
from typing import Tuple


def assignment():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def make_question_with_answer() -> Tuple[str, str]:
    question = random.randrange(1, 100)
    answer = 'no' if question % 2 else 'yes'
    return str(question), answer
