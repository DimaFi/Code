# Максимальный элемент каждой строки

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

max_elements = [max(row) for row in matrix]

print(" ".join(map(str, max_elements)))