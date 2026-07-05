import re

p = input("Password: ")

if (len(p) >= 8 and
    re.search(r"[A-Z]", p) and
    re.search(r"[a-z]", p) and
    re.search(r"\d", p)):
    print("Strong Password")
else:
    print("Weak Password")