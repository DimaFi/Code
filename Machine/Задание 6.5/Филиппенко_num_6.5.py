import time
import numpy as np

# через list
def create_matrix_list(size, input_string):
    matrix = []
    idx = 0
    for i in range(size):
        row = []
        for j in range(size):
            row.append(int(input_string[idx]))
            idx += 1
        matrix.append(row)
    return matrix

# NumPy
def create_matrix_numpy(size, input_string):
    # строку в массив
    arr = np.array([int(x) for x in input_string])
    return arr.reshape(size, size)


input_string = "1234567890" * 100000  # Строка из 100000 символов для матрицы 500x500


sizes = [10, 100, 500]

# Сравнение
for size in sizes:
    print(f"\nРазмер матрицы: {size}x{size}")
    
    required_length = size * size
    input_str_for_size = input_string[:required_length]

    if len(input_str_for_size) < required_length:
        print(f"Ошибка: строка слишком короткая для размера {size}x{size}")
        continue

    # Для list
    start_time = time.time()
    matrix_list = create_matrix_list(size, input_str_for_size)
    end_time = time.time()
    print(f"Время выполнения через list: {end_time - start_time:.6f} секунд")
    
    # Для NumPy
    start_time = time.time()
    matrix_numpy = create_matrix_numpy(size, input_str_for_size)
    end_time = time.time()
    print(f"Время выполнения через NumPy: {end_time - start_time:.6f} секунд")
