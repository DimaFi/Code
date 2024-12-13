import numpy as np
from scipy.optimize import minimize_scalar

# Целевая функция
def objective_function(x):
    x1, x2 = x[0], x[1]
    return 100 * x1 ** 2 - 23 * x1 * x2 + 111 * x2 ** 2 - 17 * x1 + 13 * x2 + 10

# Вычисление градиента
def compute_gradient(x):
    x1, x2 = x[0], x[1]
    grad_x1 = 200 * x1 - 23 * x2 - 17
    grad_x2 = 222 * x2 - 23 * x1 + 13
    return np.array([grad_x1, grad_x2])

# Метод наискорейшего спуска
def fastest_descent(func, grad_func, x0, tolerance=1e-6, max_iterations=1000):
    x = x0
    path = [x]
    for _ in range(max_iterations):
        grad = grad_func(x)
        # Определение оптимального шага с помощью минимизации одномерной функции
        optimal_step = minimize_scalar(lambda step: func(x - step * grad)).x
        # Обновление текущей точки
        x_new = x - optimal_step * grad
        path.append(x_new)
        # Проверка условия сходимости
        if np.linalg.norm(x_new - x) < tolerance:
            break
        x = x_new
    return x, len(path)

# Начальная точка
x0 = np.array([0.0, 0.0])

result, iterations = fastest_descent(objective_function, compute_gradient, x0)

print(f"Минимум функции достигается в точке: {result}")
print(f"Количество итераций: {iterations}")
print(f"Значение функции в найденной точке: {objective_function(result)}")

