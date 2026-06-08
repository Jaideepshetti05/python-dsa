num = int(input())

temp = num
total = 0

while temp:
    digit = temp % 10
    total += digit ** 3
    temp //= 10

print(total == num)