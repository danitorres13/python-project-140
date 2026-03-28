from brain_games.cli import welcome_user
import random
import prompt 

def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        num = random.randint(1, 100)
        print(f"Question: {num}")
        answer = prompt.string("Your answer: ")
        if num % 2 == 0:
            correct_answer = "yes"
        else:
            correct_answer = "no" 
    
        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")

