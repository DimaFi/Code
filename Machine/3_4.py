n = int(input())
n1 = 0
c1 = 0
cmax = 1
nnow = 0

for i in range(n):
    a = int(input())
    if c1 == 0:
        nnow = a
    if nnow == a:
        c1 += 1
    else:
        nnow = a
        c1 = 1
    if c1 > cmax:
        cmax = c1

print(cmax)
