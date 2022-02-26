import random

def guess(x):
    random_num = random.randint(1, x)
    guess = 0
    while guess != random_num:
        guess = int(input(f"Guess any number between 1 and {x}: "))
        print(random_num)

guess(int(input("Enter Number Boundary")))