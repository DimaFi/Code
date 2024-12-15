n = int(input())
S = 0

for k in range(1, n + 1):
    sum_k = k * (k + 1) // 2
    S += (-1) ** (k + 1) * (sum_k ** 2)

print(S)
