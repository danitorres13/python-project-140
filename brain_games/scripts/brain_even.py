from brain_games.engine import run_game
from brain_games.games.brain_even import generate_round

def main():
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_game(generate_round, rules)