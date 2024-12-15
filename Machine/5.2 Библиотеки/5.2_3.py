n = int(input())
coordinates = []
current_position = 0

for i in range(1, n + 1):
    jump_length = i * (i + 1) // 2
    current_position += jump_length
    coordinates.append(current_position)

print(" ".join(map(str, coordinates)))
