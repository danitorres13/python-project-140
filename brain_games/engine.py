import prompt
from brain_games.cli import welcome_user


def run_game(game_logic, rules):
    name = welcome_user()
    print(rules)

    ROUNDS_COUNT = 3
    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game_logic()

        print(f"Question: {question}")
        print("Your answer: ", end="")
        answer = prompt.string()

        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'."
                  )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")