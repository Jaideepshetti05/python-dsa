contacts = {}

while True:
    name = input("Name: ")
    phone = input("Phone: ")

    contacts[name] = phone

    choice = input("Add more? yes/no: ")

    if choice == "no":
        break

print(contacts)