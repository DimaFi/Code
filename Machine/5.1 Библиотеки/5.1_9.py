from math import log, sqrt
x, y = map(float, input().split())
print(log(abs(abs(y-sqrt(abs(x)))*(x-y/(x+(x*x)/4)))))