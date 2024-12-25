from math import sin


def f(x: float) -> float:
    return x*x*x - sin(x)


a, b, h = map(float, input().split())
while a - 1e-10 < b:
    print(f(a), end=' ')
    a += h