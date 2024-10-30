def restore_array(n, p, q, arr):
    # сдвиг на q всего массива
    arr = arr[q:] + arr[:q]

    # делим на 2 части массив
    left_part = arr[:n//2]
    right_part = arr[n//2:]

    # обратный сдвиг левой и правой части на p
    left_part = left_part[p:] + left_part[:p]
    right_part = right_part[p:] + right_part[:p]

    restored_arr = left_part + right_part
    return restored_arr

n, p, q = map(int, input().split())
arr = list(map(int, input().split()))
result = restore_array(n, p, q, arr)
print(" ".join(map(str, result)))
