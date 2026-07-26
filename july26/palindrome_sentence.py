s = input().lower()

clean = ''.join(c for c in s if c.isalnum())

print(clean == clean[::-1])