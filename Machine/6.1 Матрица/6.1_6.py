# Линии из звездочек

n, m = map(int, input().split())
field = [input().strip() for _ in range(n)]

# строки
row_count = sum(1 for row in field if row == '*' * m)

# столбцы
col_count = 0
for col in range(m):
    if all(field[row][col] == '*' for row in range(n)):
        col_count += 1

print(row_count + col_count)
