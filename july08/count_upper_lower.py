text = input()

upper = sum(c.isupper() for c in text)
lower = sum(c.islower() for c in text)

print("Upper:", upper)
print("Lower:", lower)