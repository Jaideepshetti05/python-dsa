a = []

for _ in range(2):
    a.append(list(map(int, input().split())))

b = []

for _ in range(2):
    b.append(list(map(int, input().split())))

for i in range(2):
    for j in range(2):
        print(a[i][j] + b[i][j], end=" ")
    print()