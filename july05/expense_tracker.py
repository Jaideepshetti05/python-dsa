expenses = []

while True:
    item = input("Expense (or 'done'): ")
    if item.lower() == "done":
        break
    amount = float(input("Amount: "))
    expenses.append((item, amount))

total = sum(amount for _, amount in expenses)

print("Total Expense =", total)