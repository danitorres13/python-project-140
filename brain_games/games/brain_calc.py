import random  


def generate_round():
    num1 = random.randint(1, 100)  # Sensitive
    num2 = random.randint(1, 100)  # Sensitive 
    symbol = random.choice(["+", "-", "*"])  # Sensitive

    question = f"{num1} {symbol} {num2}"

    if symbol == "+":
        correct_answer = num1 + num2
    elif symbol == "-":
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2

    return question, str(correct_answer)

