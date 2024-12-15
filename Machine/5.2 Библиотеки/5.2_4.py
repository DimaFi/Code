from itertools import product

n = int(input())

# создаем перестановки с повторениями
elements = range(1, n + 1)
permutations = list(product(elements, repeat=n))

print(len(permutations))

for perm in permutations:
    print(" ".join(map(str, perm)))
