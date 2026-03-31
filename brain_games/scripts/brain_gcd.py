from brain_games.engine import run_game
from brain_games.games.brain_gcd import generate_round


def main():
    rules = 'Find the greatest common divisor of given numbers.'
    run_game(generate_round, rules)