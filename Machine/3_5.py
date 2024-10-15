a, b = map(int, input().split())

sum = 0
nb = 1
c = 0
a1 = a

while a1 < b:
    a1 *= 3
    nb += 1

while sum < 1000000:
    c += 1
    sum += a
    a = a * 3

print(int(nb), int(c))