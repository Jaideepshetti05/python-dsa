inventory = {
    "Keyboard": 10,
    "Mouse": 15,
    "Monitor": 5
}

while True:

    print("\nInventory Menu")
    print("1. View")
    print("2. Add Product")
    print("3. Update Quantity")
    print("4. Exit")

    ch = input("Choice: ")

    if ch == "1":

        for product, qty in inventory.items():
            print(product, ":", qty)

    elif ch == "2":

        product = input("Product Name: ")
        qty = int(input("Quantity: "))
        inventory[product] = qty

    elif ch == "3":

        product = input("Product Name: ")

        if product in inventory:
            inventory[product] = int(input("New Quantity: "))
        else:
            print("Product not found.")

    elif ch == "4":
        break

    else:
        print("Invalid choice.")