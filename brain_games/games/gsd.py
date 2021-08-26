import operator
import random
from typing import Tuple


def assignment():
    return 'Find the greatest common divisor of given numbers.'


def make_question_with_answer() -> Tuple[str, str]:
    operand1 = random.randrange(1, 50)
    operand2 = random.randrange(1, 50)
    question = f'{operand1} {operand2}'
    answer = greatest_common_divisor(operand1, operand2)
    return question, str(answer)


def greatest_common_divisor(
    num1: int,
    num2: int,
) -> int:
    if not num2:
        return num1
    return greatest_common_divisor(num2, num1 % num2)