import random
from typing import Tuple


def assignment():
    return 'What number is missing in the progression?'


def make_question_with_answer() -> Tuple[str, str]:
    start = random.randint(1, 50)
    step = random.randint(1, 20)
    length = 10

    progression = list(range(start, (start + length * step), step))

    hidden_index = random.randrange(0, length)
    answer, progression[hidden_index] = progression[hidden_index], '..'
    question = ' '.join(map(str, progression))

    return question, str(answer)
