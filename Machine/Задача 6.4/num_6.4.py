import numpy as np


def build_array(base_array, N):
    current_array = base_array
    while current_array.shape[0] < N:
        # Горизонтальное отражение и добавление справа
        current_array = np.concatenate((current_array, np.fliplr(current_array)), axis=1)
        # Вертикальное отражение и добавление сверху
        current_array = np.concatenate((np.flipud(current_array), current_array), axis=0)
    return current_array

base_array = np.array([
    ['A', 'B', 'C'],
    ['B', 'C', 'A'],
    ['C', 'A', 'B']
])

N = 192

res_array = build_array(base_array, N)


x, y = 100, 150
value = res_array[x, y]

print(f"Значение элемента с индексами [{x}, {y}]: {value}")
