n = int(input())
n1 = 0
c1 = 0
cmax = 0
nnow = 0

for i in range(n):
    a = int(input())
    nnow = a
    if  nnow == a:
        c1 += 1
    else:
        c1 = 0
    if c1 >= cmax:
        cmax = c1
        c1 = 0

print(cmax)
