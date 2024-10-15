n = int(input())

a = []
c = 2

while n != 1:
    if n % c == 0:
        a.append(c)
        n //= c
    else:
        c += 1

print(*a) 