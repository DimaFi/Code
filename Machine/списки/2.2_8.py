def reverse_segment(n, arr):
    # индекс левого минимума
    min_value = min(arr)
    left_min_index = arr.index(min_value)

    # индекс правого максимума
    max_value = max(arr)
    right_max_index = len(arr) - 1 - arr[::-1].index(max_value)

    # инвертируем порядок элементов на участке между left_min_index и right_max_index
    if left_min_index <= right_max_index:
        arr[left_min_index:right_max_index + 1] = arr[left_min_index:right_max_index + 1][::-1]

    return arr

n = int(input())
arr = list(map(int, input().split()))
result = reverse_segment(n, arr)
print(" ".join(map(str, result)))
