def is_power_of_five(num):
    if num < 1:
        return False
    while num % 5 == 0:
        num //= 5
    return num == 1

def count_powers_of_five(numbers):
    count = 0
    for num in numbers:
        if is_power_of_five(num):
            count += 1
    return count

N = int(input())
numbers = list(map(int, input().split()))

result = count_powers_of_five(numbers)

print(result)
