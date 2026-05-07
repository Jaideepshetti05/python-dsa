import random

num = random.randint(1, 10)

guess = int(input("Guess number: "))

if guess == num:
    print("Correct")
else:
    print("Wrong. Number was", num)