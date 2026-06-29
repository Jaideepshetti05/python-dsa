import re

def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"\d", password):
        score += 1

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    levels = {
        5: "Very Strong",
        4: "Strong",
        3: "Medium"
    }

    return levels.get(score, "Weak")


password = input("Enter Password: ")
print("Password Strength:", check_password(password))