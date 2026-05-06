import random

while True:
    choice = input("Roll dice? (y/n): ")

    if choice == 'y':
        print("Dice:", random.randint(1, 6))
    else:
        break