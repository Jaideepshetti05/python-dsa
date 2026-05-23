expenses = []

for i in range(5):
    amount = float(input("Enter expense: "))
    expenses.append(amount)

print("Total Expense:", sum(expenses))