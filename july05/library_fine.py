days = int(input("Days Late: "))

if days <= 5:
    fine = days * 2
elif days <= 10:
    fine = 10 + (days - 5) * 5
else:
    fine = 35 + (days - 10) * 10

print("Fine =", fine)