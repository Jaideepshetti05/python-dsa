# File: armstrong.py

num = int(input("Enter number: "))

power = len(str(num))
total = 0
temp = num

while temp > 0:
    digit = temp % 10
    total += digit ** power
    temp //= 10

print("Armstrong" if total == num else "Not Armstrong")