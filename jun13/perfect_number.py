n = int(input())

s = sum(i for i in range(1, n) if n % i == 0)

if s == n:
    print("Perfect Number")
else:
    print("Not Perfect Number")