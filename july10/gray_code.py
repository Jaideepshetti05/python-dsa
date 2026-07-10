n = 4

for i in range(1 << n):
    print(bin(i ^ (i >> 1))[2:])