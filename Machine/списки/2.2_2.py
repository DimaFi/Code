n, m, k = map(int,input().split())
array = list(map(int, input().split()))

sum = 0


for i in range(n):
    if array[i] % m != 0 and abs(array[i]) % 10 == k:
        sum += array[i]

print(sum)
