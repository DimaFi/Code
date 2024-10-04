n = int(input())
n1max = -1
n1 = 0

max = -1

for i in range(n):
    a = int(input())
    n1 += 1
    if abs(a) >= max:
        max = abs(a)
        n1max = n1

print(n1max)
