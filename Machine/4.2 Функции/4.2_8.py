def fibonacci(k):
    a, b = 1, 1
    
    # если K = 1,2
    
    if k == 1 or k == 2:
        return 1
    
    # k > 2
    for _ in range(3, k + 1):
        a, b = b, a + b 
    
    return b

k = int(input())

print(fibonacci(k))
