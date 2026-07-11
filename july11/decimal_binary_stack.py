stack = []

n = 45

while n:
    stack.append(n % 2)
    n //= 2

while stack:
    print(stack.pop(), end="")