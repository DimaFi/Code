N = int(input())
numbers = list(map(int, input().split()))

filtered_numbers = [
    number for number in numbers
    if len(set(str(abs(number)))) != len(str(abs(number)))
]

if filtered_numbers:
    print(" ".join(map(str, filtered_numbers)))
else:
    print()
