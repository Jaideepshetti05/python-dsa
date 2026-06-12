expenses = []

for i in range(3):
    amount = float(input(f"Enter expense {i+1}: "))
    expenses.append(amount)

print("Total Expense:", sum(expenses))