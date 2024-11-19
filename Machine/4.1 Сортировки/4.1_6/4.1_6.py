n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# трансопнируем и все столбцы станут строками
transposed = list(zip(*matrix))

for i in range(len(transposed)):
    if i % 2 == 0:
        transposed[i] = sorted(transposed[i])
    else:
        transposed[i] = sorted(transposed[i], reverse=True) 

result = list(zip(*transposed))

for row in result:
    print(" ".join(map(str, row)))
