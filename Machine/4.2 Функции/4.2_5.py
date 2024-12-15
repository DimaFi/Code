def transpose_matrix(matrix):
    # строки столбцами, а столбцы — строками.
    
    n = len(matrix) # строк в исходной
    m = len(matrix[0]) # столбцов в исходной

    # новая m x n
    transposed = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            transposed[j][i] = matrix[i][j]

    return transposed

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

transposed_matrix = transpose_matrix(matrix)


for row in transposed_matrix:
    print(*row)
