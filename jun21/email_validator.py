email = input("Email: ")

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")