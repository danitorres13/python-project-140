import random

MIN_NUMBER = 1
MAX_NUMBER = 100

def generate_round():
    num = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = str(num)
    correct_answer = "yes" if num % 2 == 0 else "no"
    return question, correct_answer