import math

sequence = []
while True:
    try:
        line = input().strip()
        if line:
            sequence.append(float(line))
        else:
            break
    except EOFError:
        break

# первый отриц элемент и ищем произведение
product = 1
for num in sequence:
    if num < 0:
        break
    product *= num

result = math.cos(product)

print(f"{result:.12f}")
