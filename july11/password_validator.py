import re

password = "Python@123"

pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$'

print(bool(re.match(pattern, password)))