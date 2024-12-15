def swap_min_and_last_in_column(matrix, col_idx):
    n = len(matrix)  # Количество строк
    min_value = matrix[0][col_idx]
    min_idx = 0

    for i in range(n):
        if matrix[i][col_idx] < min_value:
            min_value = matrix[i][col_idx]
            min_idx = i

    matrix[min_idx][col_idx], matrix[n - 1][col_idx] = matrix[n - 1][col_idx], matrix[min_idx][col_idx]

def process_matrix(matrix):
    m = len(matrix[0])  # столбцы
    for col_idx in range(m):
        swap_min_and_last_in_column(matrix, col_idx)

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

process_matrix(matrix)

for row in matrix:
    print(*row)
