num = 28
total = sum(i for i in range(1, num) if num % i == 0)

if total == num:
    print("Perfect Number")
else:
    print("Not Perfect")