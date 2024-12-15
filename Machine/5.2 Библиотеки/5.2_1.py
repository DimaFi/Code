n = int(input())
result = []
current_position = 0

for i in range(1, n + 1):
    current_position += i
    result.append(current_position)

print(" ".join(map(str, result)))
