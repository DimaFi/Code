from itertools import combinations

n, m = map(int, input().split())

# сочетания из n по m
combs = combinations(range(1, n + 1), m)

combs_list = list(combs)

print(len(combs_list))

for comb in combs_list:
    print(" ".join(map(str, comb)))
