import numpy as np

def objective_function(x):
    x1, x2 = x[0], x[1]
    return 100 * x1 ** 2 - 23 * x1 * x2 + 111 * x2 ** 2 - 17 * x1 + 13 * x2 + 10

def grad_f(x):
    x1, x2 = x[0], x[1]
    grad_x1 = 200 * x1 - 23 * x2 - 17
    grad_x2 = 222 * x2 - 23 * x1 + 13
    return np.array([grad_x1, grad_x2])

def hessian_f():
    return np.array([[200, -23],
                     [-23, 222]])       

def newton_method(x0, tol=1e-6, max_iter=1000):
    x = x0
    H = hessian_f()
    for i in range(max_iter):
        grad = grad_f(x)
        if np.linalg.norm(grad) < tol:
            return x, i
        x = x - np.dot(np.linalg.inv(H), grad)
    return x, max_iter

x0 = np.array([0.0, 0.0])

newton_result, newton_iterations = newton_method(x0)

print(f"Минимум функции методом Ньютона достигается в точке: {newton_result}")
print(f"Количество итераций: {newton_iterations}")
print(f"Значение функции в найденной точке: {objective_function(newton_result)}")
