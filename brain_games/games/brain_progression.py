import random  # nosec


def generate_round():
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    length = 10

    progression = []

    for i in range(length):
        progression.append(start + i * step)

    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]

    progression[hidden_index] = ".."

    question = " ".join(map(str, progression))

    return question, str(correct_answer)