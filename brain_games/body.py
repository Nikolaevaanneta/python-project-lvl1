import prompt


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')

    print(game.assignment())

    game_rounds_count = 3
    for round_number in range(0, game_rounds_count):
        question, correct_answer = game.make_question_with_answer()
        print(f'Question: {question}')

        user_answer = prompt.string('Your answer: ')
        if correct_answer != user_answer:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return
        print('Correct!')

    print(f'Congratulations, {name}!')
