import math

N = int(input())

a = round(N ** (1 / 3))

if a ** 3 == N:
    is_prime = True
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            is_prime = False
            break
    if is_prime and a > 1:
        print("Yes")
    else:
        print("No")
else:
    print("No")
