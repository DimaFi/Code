from math import pi
r = float(input())
R = float(input())
print(f"{max(0, pi*max(r, R)*max(R, r) - pi*min(r, R)*min(r, R))}")