# File: matrix_addition.py
r = int(input())
c = int(input())

a = []
b = []

for _ in range(r):
    a.append(list(map(int, input().split())))

for _ in range(r):
    b.append(list(map(int, input().split())))

for i in range(r):
    for j in range(c):
        print(a[i][j] + b[i][j], end=" ")
    print()