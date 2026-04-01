import random  # nosec


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def generate_round():
    num = random.randint(1, 100)

    question = str(num)

    if is_prime(num):
        correct_answer = "yes"
    else:
        correct_answer = "no"

    return question, str(correct_answer)