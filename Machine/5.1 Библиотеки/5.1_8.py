from math import tan, e
x, y = map(float, input().split())
print((1+e**(y-1))/(1 + x*x*abs(y-tan(x))))