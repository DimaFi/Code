N = int(input())
numbers = [input().strip() for _ in range(N)]

suitable_numbers = []

for i in range(N - 1):
    current_number = numbers[i]
    next_number = numbers[i + 1]

    current_digits = set(current_number)
    next_digits = set(next_number)
    
    common_digits = current_digits & next_digits
    
    if len(common_digits) == 2:
        suitable_numbers.append(current_number)

if suitable_numbers:
    for number in suitable_numbers:
        print(number)
else:
    print("N")
