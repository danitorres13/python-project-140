import random # nosec
import math # nosec


def generate_round():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    question = f"{num1} {num2}"
    correct_answer = math.gcd(num1, num2)

    return question, str(correct_answer)