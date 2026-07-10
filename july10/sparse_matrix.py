matrix = [
    [0,0,3],
    [0,0,0],
    [5,0,0]
]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]:
            print(i, j, matrix[i][j])