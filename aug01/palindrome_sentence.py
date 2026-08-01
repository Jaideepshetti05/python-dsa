import re

s = "A man a plan a canal Panama"

s = re.sub(r'[^A-Za-z0-9]', '', s).lower()

print(s == s[::-1])