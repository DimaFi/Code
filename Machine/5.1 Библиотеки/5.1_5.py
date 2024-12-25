from math import sqrt


def rec(n: int, cur: int) -> float:
    if (cur == n):
        return n
    else:
        if (cur == 1):
            return n / sqrt(1 + sqrt(rec(n, cur+1)))
        else:
            return cur + sqrt(rec(n, cur+1))


n = int(input())
print(rec(n, 1))