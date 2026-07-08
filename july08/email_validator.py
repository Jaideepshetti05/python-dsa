import re

email = input("Enter Email: ")

if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
    print("Valid Email")
else:
    print("Invalid Email")