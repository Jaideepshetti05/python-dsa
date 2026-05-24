r = int(input())
c = int(input())

a = []
b = []

for i in range(r):
    row = list(map(int, input().split()))
    a.append(row)

for i in range(r):
    row = list(map(int, input().split()))
    b.append(row)

for i in range(r):
    for j in range(c):
        print(a[i][j] + b[i][j], end=" ")
    print()