from brain_games.engine import run_game
from brain_games.games.brain_progression import generate_round


def main():
    rules = 'What number is missing in the progression?'
    run_game(generate_round, rules)