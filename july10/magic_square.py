matrix = [
    [8,1,6],
    [3,5,7],
    [4,9,2]
]

target = sum(matrix[0])

valid = True

for row in matrix:
    if sum(row) != target:
        valid = False

for col in zip(*matrix):
    if sum(col) != target:
        valid = False

print(valid)