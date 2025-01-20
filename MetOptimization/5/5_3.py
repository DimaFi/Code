import numpy as np

def objective_function(x):
    x1, x2 = x[0], x[1]
    return 100 * x1 ** 2 - 23 * x1 * x2 + 111 * x2 ** 2 - 17 * x1 + 13 * x2 + 10

def compute_gradient(x):
    x1, x2 = x[0], x[1]
    grad_x1 = 200 * x1 - 23 * x2 - 17
    grad_x2 = 222 * x2 - 23 * x1 + 13
    return np.array([grad_x1, grad_x2])

def compute_hessian(x):
    # return np.array([[264, -115],[-115, 264]])
    return np.array([[200, -23],
                     [-23, 222]])

# Метод Ньютона
def newton_optimization(func, grad_func, hessian_func, x0, tolerance=1e-6, max_iterations=1000):
    x = x0
    path = [x]
    for _ in range(max_iterations):
        grad = grad_func(x)  # Вычисляем градиент
        hessian = hessian_func(x)  # Вычисляем гессиан
        # Решаем систему линейных уравнений: H(x) * Δx = -grad(x)
        delta_x = np.linalg.solve(hessian, -grad)
        x_new = x + delta_x  # Обновляем точку
        path.append(x_new)
        # Проверка сходимости
        if np.linalg.norm(x_new - x) < tolerance:
            break
        x = x_new
    return x, len(path)

x0 = np.array([0.0, 0.0])

newton_result, newton_iterations = newton_optimization(objective_function, compute_gradient, compute_hessian, x0)

print(f"Минимум функции методом Ньютона достигается в точке: {newton_result}")
print(f"Количество итераций: {newton_iterations}")
print(f"Значение функции в найденной точке: {objective_function(newton_result)}")
