import re

email = "abc@gmail.com"

pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

print("Valid" if re.match(pattern, email) else "Invalid")