for num in range(1, 1001):
    digits = len(str(num))
    total = sum(int(d) ** digits for d in str(num))
    if total == num:
        print(num)