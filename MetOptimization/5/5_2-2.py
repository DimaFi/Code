import numpy as np

def objective_function(x):
    x1, x2 = x[0], x[1]
    return 100 * x1 ** 2 - 23 * x1 * x2 + 111 * x2 ** 2 - 17 * x1 + 13 * x2 + 10

def compute_gradient(x):
    x1, x2 = x[0], x[1]
    grad_x1 = 200 * x1 - 23 * x2 - 17
    grad_x2 = 222 * x2 - 23 * x1 + 13
    return np.array([grad_x1, grad_x2])

def compute_hessian():
    return np.array([[200, -23],
                     [-23, 222]])

def steepest_descent(x0, tol=1e-6, max_iter=1000):
    x = x0
    for i in range(max_iter):
        grad = compute_gradient(x)
        if np.linalg.norm(grad) < tol:
            return x, i
        hessian = compute_hessian()
        alpha = -np.dot(grad, grad) / np.dot(grad.T, hessian @ grad)
        x = x + alpha * grad
    return x, max_iter

x0 = np.array([0.0, 0.0])

result, iterations = steepest_descent(x0)

print(f"Минимум функции достигается в точке: {result}")
print(f"Количество итераций: {iterations}")
print(f"Значение функции в найденной точке: {objective_function(result)}")
