num = 84
i = 2

while i <= num:
    while num % i == 0:
        print(i, end=" ")
        num //= i
    i += 1