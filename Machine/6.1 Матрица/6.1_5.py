# Четные и нечетные числа столбца

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

for col in range(n):
    even_count = 0  # чет
    odd_count = 0   # нечет
    for row in range(n):
        if matrix[row][col] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print(even_count, odd_count)