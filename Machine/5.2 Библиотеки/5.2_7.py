from itertools import permutations

n = int(input())

perm = permutations(range(1, n + 1)) # перестановки

perm_list = list(perm)
print(len(perm_list))

for p in perm_list:
    print(" ".join(map(str, p)))
