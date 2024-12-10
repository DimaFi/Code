import numpy as np

# 1. Сгенерировать матрицу размером 2 × 12, заполненную целыми числами.
matrix = np.random.randint(1, 100, size=(2, 12))
print("Матрица 2x12:\n", matrix)

# 2. Вывести на экран элемент с индексами [1, 5].
element_1_5 = matrix[1, 5]
print("Элемент [1, 5]: ", element_1_5)

# 3. Вывести на экран шестой столбец матрицы.
column_6 = matrix[:, 5]
print("Шестой столбец:\n", column_6)

# 4. Вывести на экран каждый третий элемент второй строки матрицы в обратном порядке.
second_row = matrix[1, ::3][::-1]
print("Каждый 3 эл в обратном порядке: ", second_row)

# 5. Изменить форму матрицы с 2 × 12 на 4 × 6.
reshaped_matrix = matrix.reshape(4, 6)
print("Матрица на 4x6:\n", reshaped_matrix)

# 6. Разделить каждый элемент матрицы на заданное число (например, 2).
divided_matrix = reshaped_matrix / 2
print("Все элементы на 2:\n", divided_matrix)

# 7. Найти максимум в каждом столбце.
column_max = reshaped_matrix.max(axis=0)
print("Макс в каждом столбце:\n", column_max)

# 8. Найти минимальный элемент в первой строке.
min_in_first_row = reshaped_matrix[0, :].min()
print("Мин элемент в первой строке: ", min_in_first_row)

# 9. Определить, образуют ли элементы массива перед первым отрицательным возрастающую последовательность.
array = np.random.randint(-10, 10, size=15)
print("\nОдномерный массив:", array)
negative_index = np.where(array < 0)[0]
if len(negative_index) > 0:
    sub_array = array[:negative_index[0]]
    is_increasing = np.all(np.diff(sub_array) > 0)  # вычисляем разность между всеми парами  ипроверяем что все они > 0
    print("Послед перед 1 отрицательным: ", sub_array)
    print("Образует возрастающую последовательность:", is_increasing)
else:
    print("В массиве нет отриц")

# 10. Выяснить, является ли сумма элементов, расположенных над нулями, четным числом.
matrix_10 = np.random.randint(-5, 5, size=(5, 5))
print("Матрица 5x5:\n", matrix_10)
zero_indices = np.where(matrix_10 == 0)
if len(zero_indices[0]) > 0:
    sum_above_zeros = 0
    for row, col in zip(zero_indices[0], zero_indices[1]):
        if row > 0:
            sum_above_zeros += matrix_10[row - 1, col]
    print("Сумма элементов над 0: ", sum_above_zeros)
    print("Сумма четнаое? : ", sum_above_zeros % 2 == 0)
else:
    print("В матрице нет нулей")
