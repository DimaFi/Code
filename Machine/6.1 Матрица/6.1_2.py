# Максимальный элемент каждого столбца

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# в отличие от первой, нужно создать 2 цикла для столбцов, а потом элементов внутри солбца
max_elements = [max(matrix[row][col] for row in range(n)) for col in range(n)]

print(" ".join(map(str, max_elements)))