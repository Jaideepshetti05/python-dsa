import time, os

file = "test.txt"
last_modified = os.path.getmtime(file)

while True:
    current = os.path.getmtime(file)
    if current != last_modified:
        print("File modified!")
        last_modified = current
    time.sleep(2)