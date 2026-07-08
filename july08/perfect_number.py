n = int(input())

total = sum(i for i in range(1, n) if n % i == 0)

if total == n:
    print("Perfect")
else:
    print("Not Perfect")