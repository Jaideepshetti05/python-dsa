import re

pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

email = input("Enter Email: ")

if re.fullmatch(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")