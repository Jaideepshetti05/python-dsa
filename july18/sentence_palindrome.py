import re

s = "Madam In Eden Im Adam"

clean = re.sub(r'[^A-Za-z]', '', s).lower()

print(clean == clean[::-1])