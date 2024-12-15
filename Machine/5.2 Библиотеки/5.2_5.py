from itertools import product

n, k = map(int, input().split())

elements = range(1, n + 1)
placements = list(product(elements, repeat=k))

print(len(placements))

for placement in placements:
    print(" ".join(map(str, placement)))
