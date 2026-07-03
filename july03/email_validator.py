    import re

email = "abc@gmail.com"

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

print(bool(re.match(pattern, email)))