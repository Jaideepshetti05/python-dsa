import re

pwd = input("Enter password: ")

if len(pwd) >= 8 and re.search(r"\d", pwd) and re.search(r"[A-Z]", pwd):
    print("Strong Password")
else:
    print("Weak Password")