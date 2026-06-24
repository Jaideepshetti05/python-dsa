n = int(input("Enter number: "))

i = 2
while i <= n:
    while n % i == 0:
        print(i, end=" ")
        n //= i
    i += 1