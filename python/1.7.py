# Rotate a matrix, can you do it in place
import numpy as np

m = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

n = np.array([[ 1, 2, 3, 4, 5],
              [ 6, 7, 8, 9,10],
              [11,12,13,14,15],
              [16,17,18,19,20],
              [21,22,23,24,25]])

def rotate(matrix):
    if matrix.shape[0] != matrix.shape[1]: return matrix
    for index in range(int(matrix.shape[0]/2)):
        for item in range(index, matrix.shape[0]-1-index):
            temp = matrix[index][item+index]
            matrix[index][item+index] = matrix[item+index][matrix.shape[1]-1-index]
            matrix[item+index][matrix.shape[1]-1-index] = matrix[matrix.shape[0]-1-index][matrix.shape[1]-item-1-index]
            matrix[matrix.shape[0]-1-index][matrix.shape[1]-item-1-index] = matrix[matrix.shape[1]-item-1-index][index]
            matrix[matrix.shape[1]-item-1-index][index] = temp
    return matrix

print(m)
print(rotate(m))
print(n)
print(rotate(n))
