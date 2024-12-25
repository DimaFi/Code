from math import log, sqrt
a = [float(input()) for i in range(3)]

p = (a[0] + a[1] + a[2])/2
if a[0]+a[1] <= a[2] or a[0] + a[2] <= a[1] or a[2] + a[1] <= a[0]:
    print(0)
else:
    s = sqrt(p*(p-a[0])*(p-a[1])*(p-a[2]))
    a = sorted(a)
    print((a[0]*a[1]*a[2])/(4*s) if a[2]*a[2] < a[0] *
          a[0]+a[1]*a[2] else max(a[0], a[1], a[2])/2)