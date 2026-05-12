num = 987654
count = 0

while num > 0:
    num //= 10
    count += 1

print("Digits:", count)