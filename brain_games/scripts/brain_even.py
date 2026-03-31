import random # nosec
import prompt
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(3):
        num = random.randint(1, 100)
        print(f"Question: {num}")
        answer = prompt.string("Your answer: ")

        correct_answer = "yes" if num % 2 == 0 else "no"

        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'."
                  )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
