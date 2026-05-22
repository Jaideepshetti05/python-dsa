# File: sum_of_digits.py

num = int(input("Enter number: "))

sum_digits = 0

while num > 0:
    sum_digits += num % 10
    num //= 10

print("Sum:", sum_digits)