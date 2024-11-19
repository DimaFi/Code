n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    matrix[i].sort(reverse=True)

for row in matrix:
    print(" ".join(map(str, row)))
