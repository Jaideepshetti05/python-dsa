text = "Python Programming"

upper = sum(1 for c in text if c.isupper())
lower = sum(1 for c in text if c.islower())

print("Upper:", upper)
print("Lower:", lower)