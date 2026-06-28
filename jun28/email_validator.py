import re

email=input()

print(bool(re.match(r"^[A-Za-z0-9+_.-]+@(.+)$",email)))