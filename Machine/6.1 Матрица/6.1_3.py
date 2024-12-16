# Главная диагональ

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

diagonal = [matrix[i][i] for i in range(n)]

print(" ".join(map(str, diagonal)))