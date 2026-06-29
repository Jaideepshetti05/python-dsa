expenses = []

while True:

    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":

        category = input("Category: ")
        amount = float(input("Amount: "))

        expenses.append((category, amount))

    elif choice == "2":

        for category, amount in expenses:
            print(f"{category} : ₹{amount}")

    elif choice == "3":

        total = sum(amount for _, amount in expenses)

        print("Total Expenses = ₹", total)

    elif choice == "4":

        break

    else:
        print("Invalid Choice")