def multiply_matrices(mat1, mat2):
    # матрица на матрицу
    n = len(mat1)
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result


def matrix_power(matrix, power):
    # матрицу в степень n
    
    n = len(matrix)
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]  # ед матрица

    for _ in range(power):
        result = multiply_matrices(result, matrix)

    return result


n = int(input())
matrix = [list(map(float, input().split())) for _ in range(n)]

result_matrix = matrix_power(matrix, n)


for row in result_matrix:
    print(" ".join(f"{x:.3f}" for x in row))
