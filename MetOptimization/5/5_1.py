import numpy as np

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

def adaptive_gradient_descent(func, grad_func, x0, tolerance=1e-6, max_iterations=1000, initial_step=0.1):
    x = x0
    step_size = initial_step
    path = [x]
    for _ in range(max_iterations):
        grad = grad_func(x)
        grad_norm = np.linalg.norm(grad)
        if grad_norm < tolerance: #∥∇f(x)∥<ϵ
            break
        x_new = x - step_size * grad / grad_norm #y=x−α∇f(x)
        if func(x_new) > func(x):  # Уменьшаем шаг, если значение функции увеличивается
            step_size *= 0.5
        else:
            path.append(x_new)
            if np.linalg.norm(x_new - x) < tolerance:
                break
            x = x_new
    return x, len(path)


# x0 = np.array([0.0, 0.0])
# gradient_result = adaptive_gradient_descent(objective_function, compute_gradient, x0)


x0 = np.array([0.0, 0.0])  # Начальная точка
result, iterations = adaptive_gradient_descent(objective_function, compute_gradient, x0)

print(f"Минимум функции достигается в точке: {result}")
print(f"Количество итераций: {iterations}")
print(f"Значение функции в найденной точке: {objective_function(result)}")