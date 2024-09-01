import numpy as np

# Функция для вычисления таблицы разделённых разностей
def divided_differences(x, y):
    n = len(x)
    # Создаем таблицу для разделённых разностей, инициализируем её значениями y
    dd_table = np.zeros((n, n))
    dd_table[:, 0] = y  # Первая колонка — значения функции

    # Заполняем таблицу разделённых разностей
    for j in range(1, n):
        for i in range(n - j):
            dd_table[i, j] = (dd_table[i + 1, j - 1] - dd_table[i, j - 1]) / (x[i + j] - x[i])

    return dd_table

# Функция для интерполяции многочленом Ньютона
def newton_polynomial(x, y, x_values):
    # Получаем таблицу разделённых разностей
    dd_table = divided_differences(x, y)
    n = len(x)
    result = []

    # Для каждой новой точки x_value находим приближённое значение функции
    for x_val in x_values:
        # Начальное значение многочлена — это y0 (разделённая разность нулевого порядка)
        polynomial = dd_table[0, 0]
        # Множитель для членов вида (x - x0)(x - x1)...
        multiplier = 1

        for i in range(1, n):
            multiplier *= (x_val - x[i - 1])  # (x - x0)(x - x1)...(x - xi-1)
            polynomial += dd_table[0, i] * multiplier  # Прибавляем следующий член многочлена

        result.append(polynomial)

    return result

# Данные
x = np.array([0, 1, 2, 3])
V = 12.0
y = np.array([V, 1 + V, 8 + V, 27 + V])

# Точки для интерполяции
x_values_to_interpolate = [0.5, 1.5, 2.5]

# Вычисление значений по методу Ньютона
interpolated_values = newton_polynomial(x, y, x_values_to_interpolate)

# Вывод результатов
for x_val, y_val in zip(x_values_to_interpolate, interpolated_values):
    print(f"Приближённое значение функции в точке x = {x_val}: y = {y_val}")