import prompt
from brain_games.cli import welcome_user


def run_game(game_logic, rules):
    name = welcome_user()
    print(rules)

    for _ in range(3):
        question, correct_answer = game_logic()

        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")

        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")