import re

email = input("Enter email: ")

pattern = r'^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$'

if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")