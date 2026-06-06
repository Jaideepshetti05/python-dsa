num = 84
factor = 2

while factor <= num:
    while num % factor == 0:
        print(factor, end=" ")
        num //= factor
    factor += 1