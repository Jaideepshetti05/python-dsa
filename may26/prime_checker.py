# File: prime_checker.py
n = int(input())

prime = True

if n <= 1:
    prime = False

for i in range(2, n // 2 + 1):
    if n % i == 0:
        prime = False
        break

print("Prime" if prime else "Not Prime")