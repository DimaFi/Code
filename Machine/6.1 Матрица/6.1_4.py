# Побочная диагональ

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

anti_diagonal = [matrix[i][n - 1 - i] for i in range(n)]

print(" ".join(map(str, anti_diagonal)))