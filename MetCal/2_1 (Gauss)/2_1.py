import numpy as np

def gauss_method(matrix, rhs):
    """

    :param matrix: матрица коэффициентов системы (размер n x n)
    :param rhs: вектор правых частей (размер n)
    :return: решение системы в виде вектора (размер n)
    """
    n = len(matrix)

    aug_matrix = np.hstack([matrix, rhs.reshape(-1, 1)])


    # Прямой ход, делаем матрицу треугольного вида
    for i in range(n):
        # меняем местами в текущем столбце строку с макс элементом
        max_row = i + np.argmax(np.abs(aug_matrix[i:, i]))
        aug_matrix[[i, max_row]] = aug_matrix[[max_row, i]] 

        # приведение текущей строки к удобному виду, чтобы на главной позиции был 1
        aug_matrix[i] = aug_matrix[i] / aug_matrix[i, i]

        # ниже главного жлемента обнуляем, чтоб получилась треугольная матрица
        for j in range(i + 1, n):
            aug_matrix[j] -= aug_matrix[i] * aug_matrix[j, i]

    # Обратный ход
    solution = np.zeros(n)
    for i in range(n - 1, -1, -1): # проходимся снизу вверх
        solution[i] = aug_matrix[i, -1] - np.sum(aug_matrix[i, i + 1:n] * solution[i + 1:n])

    return solution

# матрица коэффициентов
A = np.array([[0, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]], dtype=float) 

b = np.array([8, -11, -3], dtype=float) # векторы правых частей

solution = gauss_method(A, b)
print("Решение системы:", solution)
