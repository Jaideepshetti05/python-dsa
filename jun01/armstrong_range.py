for num in range(1, 1001):
    power = len(str(num))
    total = sum(int(d) ** power for d in str(num))

    if total == num:
        print(num, end=" ")