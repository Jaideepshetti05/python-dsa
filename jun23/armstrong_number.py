num = 153
temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** 3
    temp //= 10

print("Armstrong" if total == num else "Not Armstrong")