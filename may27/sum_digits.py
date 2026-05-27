# sum_digits.py
n = input("Enter number: ")

total = sum(int(digit) for digit in n)

print("Sum:", total)