n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# трансопнируем и все столбцы станут строками
transposed = list(zip(*matrix))

sorted_transposed = [sorted(row) for row in transposed]

result = list(zip(*sorted_transposed))

for row in result:
    print(" ".join(map(str, row)))