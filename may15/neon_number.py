n = int(input("Enter number: "))

square = n * n
total = 0

while square > 0:
    total += square % 10
    square //= 10

if total == n:
    print("Neon Number")
else:
    print("Not Neon Number")