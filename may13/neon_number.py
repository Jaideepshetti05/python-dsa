num = int(input())

square = num * num
sum = 0

while square > 0:
    sum += square % 10
    square //= 10

if sum == num:
    print("Neon Number")
else:
    print("Not Neon Number")