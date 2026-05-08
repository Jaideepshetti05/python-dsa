password = input("Enter Password: ")

strength = 0

if len(password) >= 8:
    strength += 1
if any(c.isupper() for c in password):
    strength += 1
if any(c.islower() for c in password):
    strength += 1
if any(c.isdigit() for c in password):
    strength += 1

if strength == 4:
    print("Strong Password")
elif strength >= 2:
    print("Medium Password")
else:
    print("Weak Password")