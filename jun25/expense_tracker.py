expenses = []

n = int(input("Enter number of expenses: "))

for i in range(n):
    amount = float(input(f"Expense {i+1}: "))
    expenses.append(amount)

total = sum(expenses)
average = total / len(expenses)

print("\n------ Report ------")
print("Expenses:", expenses)
print("Total:", total)
print("Average:", average)