N = int(input())
array = [int(input()) for i in range(N)]
k = int(input())

result = [element * k for element in array]

print(" ".join(map(str, result)))
