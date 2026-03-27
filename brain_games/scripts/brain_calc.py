from brain_games.engine import run_game
from brain_games.games.brain_calc import generate_round


def main():
    rules = "What is the result of the expression?"
    run_game(generate_round, rules)