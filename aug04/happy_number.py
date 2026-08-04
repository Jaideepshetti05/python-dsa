n = 19

while n not in (1, 4):
    n = sum(int(i) ** 2 for i in str(n))

print("Happy" if n == 1 else "Not Happy")