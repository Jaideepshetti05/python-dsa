import math

n = int(input("Enter number: "))

root = int(math.sqrt(n))

if root * root == n:
    print("Perfect Square")
else:
    print("Not Perfect Square")