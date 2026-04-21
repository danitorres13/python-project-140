import random

MIN_NUMBER = 1
PROGRESSION_LENGTH = 10
START_MAX = 50
STEP_MAX = 10


def generate_round():
    start = random.randint(MIN_NUMBER, START_MAX)
    step = random.randint(1, STEP_MAX)

    progression = []

    for i in range(PROGRESSION_LENGTH):
        progression.append(start + i * step)

    hidden_index = random.randint(0, PROGRESSION_LENGTH - 1)
    correct_answer = progression[hidden_index]

    progression[hidden_index] = ".."

    question = " ".join(map(str, progression))

    return question, str(correct_answer)