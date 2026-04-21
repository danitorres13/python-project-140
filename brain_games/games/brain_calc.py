import random

MIN_NUMBER = 1
MAX_NUMBER = 100
OPERATORS = ["+", "-", "*"]


def generate_round():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    symbol = random.choice(OPERATORS)

    question = f"{num1} {symbol} {num2}"

    if symbol == "+":
        correct_answer = num1 + num2
    elif symbol == "-":
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2

    return question, str(correct_answer)