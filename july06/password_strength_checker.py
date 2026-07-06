password = input("Enter Password: ")

strength = "Weak"

if (
    len(password) >= 8
    and any(c.isupper() for c in password)
    and any(c.islower() for c in password)
    and any(c.isdigit() for c in password)
):
    strength = "Strong"

print("Password Strength:", strength)