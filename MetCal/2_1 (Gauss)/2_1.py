import numpy as np

def gauss_method(matrix, rhs):
    """
    Решение системы линейных уравнений методом Гаусса.
    
    :param matrix: матрица коэффициентов системы (размер n x n)
    :param rhs: вектор правых частей (размер n)
    :return: решение системы в виде вектора (размер n)
    """
    n = len(matrix)
    # Преобразуем в расширенную матрицу
    aug_matrix = np.hstack([matrix, rhs.reshape(-1, 1)])

    # Прямой ход
    for i in range(n):
        # Поиск главного элемента
        max_row = i + np.argmax(np.abs(aug_matrix[i:, i]))
        aug_matrix[[i, max_row]] = aug_matrix[[max_row, i]]  # Перестановка строк

        # Нормализация текущей строки (приведение главного элемента к 1)
        aug_matrix[i] = aug_matrix[i] / aug_matrix[i, i]

        # Обнуление элементов ниже главного элемента
        for j in range(i + 1, n):
            aug_matrix[j] -= aug_matrix[i] * aug_matrix[j, i]

    # Обратный ход
    solution = np.zeros(n)
    for i in range(n - 1, -1, -1):
        solution[i] = aug_matrix[i, -1] - np.sum(aug_matrix[i, i + 1:n] * solution[i + 1:n])

    return solution

# матрица коэффициентов
A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]], dtype=float) 

b = np.array([8, -11, -3], dtype=float) # векторы правых частей

solution = gauss_method(A, b)
print("Решение системы:", solution)
