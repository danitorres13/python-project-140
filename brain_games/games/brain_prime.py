import random

MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def generate_round():
    num = random.randint(MIN_NUMBER, MAX_NUMBER)

    question = str(num)
    correct_answer = "yes" if is_prime(num) else "no"

    return question, correct_answer