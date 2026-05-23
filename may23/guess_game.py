import random

number = random.randint(1, 50)

while True:
    guess = int(input("Guess Number: "))

    if guess == number:
        print("Correct!")
        break

    elif guess > number:
        print("Too High")

    else:
        print("Too Low")