n, p, q = map(int, input().split())
a = list(map(int, input().split()))


q = q % n 
a = a[-q:] + a[:-q] 

half_n = n // 2
left = a[:half_n]
right = a[half_n:]

p = p % half_n
left = left[-p:] + left[:-p]
right = right[-p:] + right[:-p]


result = left + right

print(" ".join(map(str, result)))
