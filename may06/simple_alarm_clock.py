import time

alarm = input("Set time (HH:MM:SS): ")

while True:
    current = time.strftime("%H:%M:%S")
    print(current, end="\r")

    if current == alarm:
        print("\nWake Up!")
        break