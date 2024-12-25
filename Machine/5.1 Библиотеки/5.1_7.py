from math import gcd

n = int(input())
a = list(map(int, input().split()))
result = a[0]
for i in a:
    result = gcd(result, i)
print(result)