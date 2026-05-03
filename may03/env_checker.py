import os

key = input("Enter env variable name: ")
value = os.getenv(key)

if value:
    print(f"{key} = {value}")
else:
    print("Not found")