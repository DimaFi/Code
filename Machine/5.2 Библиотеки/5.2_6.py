from itertools import product

k, p = map(int, input().split())

# Генерация всех возможных чисел длины k
candidates = product(range(p), repeat=k)

# только те, которые не с 0
valid_numbers = []
for num in candidates:
    if num[0] != 0:
        valid_numbers.append("".join(map(str, num)))

print(len(valid_numbers))
print("\n".join(valid_numbers))
