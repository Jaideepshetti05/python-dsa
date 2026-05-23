import time

alarm = input("Set alarm time (HH:MM:SS): ")

while True:
    current = time.strftime("%H:%M:%S")

    print(current)

    if current == alarm:
        print("Wake Up!")
        break

    time.sleep(1)