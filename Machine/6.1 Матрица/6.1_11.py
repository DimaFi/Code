import numpy as np

def determinant(matrix):
    return np.linalg.det(matrix)

def inverse_matrix(matrix):
    # проверяем, что матрица обратимая (det != 0)
    det = determinant(matrix)
    if abs(det) < 1e-6:
        raise ValueError("Матрица невозвратимая")
    
    # Инахождения обратной матрицы
    return np.linalg.inv(matrix)

n = int(input())
matrix = [list(map(float, input().split())) for _ in range(n)]

matrix = np.array(matrix)

try:
    inv_matrix = inverse_matrix(matrix)
    for row in inv_matrix:
        print(' '.join(f"{x:.8f}" for x in row))
except ValueError as e:
    print(e)
