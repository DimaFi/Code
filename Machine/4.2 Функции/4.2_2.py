def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_goldbach_pair(N):
    for P1 in range(2, N):
        if is_prime(P1):
            P2 = N - P1
            if P2 >= P1 and is_prime(P2):
                return P1, P2
    return None

N = int(input())

P1, P2 = find_goldbach_pair(N)

print(P1, P2)
