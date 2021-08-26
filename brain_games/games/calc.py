import operator
import random
from typing import Tuple


def assignment():
    return 'What is the result of the expression?'


def make_question_with_answer() -> Tuple[str, str]:
    operand1 = random.randrange(1, 10)
    operand2 = random.randrange(1, 10)

    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }

    operation = random.choice(list(operations.keys()))

    question = f'{operand1} {operation} {operand2}'
    answer = str(operations[operation](operand1, operand2))
    return str(question), answer
