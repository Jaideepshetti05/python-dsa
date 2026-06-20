import re

password = "Abc@1234"

if (len(password) >= 8 and
    re.search(r"[A-Z]", password) and
    re.search(r"[a-z]", password) and
    re.search(r"\d", password) and
    re.search(r"[^a-zA-Z0-9]", password)):
    print("Strong Password")
else:
    print("Weak Password")