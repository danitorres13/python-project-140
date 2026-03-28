from brain_games.engine import run_game
from brain_games.games.brain_prime import generate_round


def main():
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    run_game(generate_round, rules)