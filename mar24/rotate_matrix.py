# File: rotate_matrix.py
def rotate(matrix):
    return list(zip(*matrix[::-1]))

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))