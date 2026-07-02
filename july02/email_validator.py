import re

email = input()

if re.match(r'^[A-Za-z0-9+_.-]+@(.+)$', email):
    print("Valid")
else:
    print("Invalid")