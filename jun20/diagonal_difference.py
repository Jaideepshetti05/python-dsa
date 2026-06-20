matrix = [[1,2,3],[4,5,6],[7,8,9]]

primary = sum(matrix[i][i] for i in range(3))
secondary = sum(matrix[i][2-i] for i in range(3))

print(abs(primary - secondary))