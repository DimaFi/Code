import numpy as np

x = np.array([1, 2, 3, 4])
A = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

# инвертируем x
x_reversed = x[::-1]

new_A = A.copy()

# 
for col_index in range(1, A.shape[1], 2):
    new_A[:, col_index] *= x_reversed

matrix_sum = new_A.sum()

print("Исходная матрица A:")
print(A)
print("Модифицированная матрица new_A:")
print(new_A)
print("Сумма элементов новой матрицы:", matrix_sum)