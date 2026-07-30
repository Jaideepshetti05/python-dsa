matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

d1 = sum(matrix[i][i] for i in range(3))
d2 = sum(matrix[i][2-i] for i in range(3))

print(abs(d1-d2))