total = 0

while True:
    amt = float(input("Expense (0 to stop): "))
    if amt == 0:
        break
    total += amt

print("Total =", total)