from math import sqrt

a, b, c = int(input()), int(input()), int(input())
print(int((-b+sqrt(b*b-4*a*c))/(2*a)), int((-b-sqrt(b*b-4*a*c))/(2*a)), sep=' ')