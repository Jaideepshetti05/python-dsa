n = int(input("Enter number: "))

seen = set()

while n != 1 and n not in seen:
    seen.add(n)
    n = sum(int(digit) ** 2 for digit in str(n))

if n == 1:
    print("Happy Number")
else:
    print("Not Happy Number")