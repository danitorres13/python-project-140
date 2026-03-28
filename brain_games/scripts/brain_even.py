from brain_games.engine import run_game
import random


def generate_round():
    num = random.randint(1, 100)
    question = str(num)
    correct_answer = "yes" if num % 2 == 0 else "no"
    return question, correct_answer


def main():
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_game(generate_round, rules)
