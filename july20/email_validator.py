import re

email = input()

if re.fullmatch(r"[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+", email):
    print("Valid Email")
else:
    print("Invalid Email")