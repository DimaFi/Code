import numpy as np

V = 12  #  правая граница
n = 100  # кол-во узлов
h = V / n  # шаг

def p(x): return x**2
def q(x): return x
def f(x): return 4 * x**4 - 3 * V * x**3 + 6 * x - 2 * V

def y_exact(x): return x**2 * (x - V)

# Сетка
x = np.linspace(0, V, n+1)

# Матрица и вектор
A = np.zeros((n+1, n+1))
b = np.zeros(n+1)

# узлы
for i in range(1, n):
    A[i, i-1] = 1 / h**2 - p(x[i]) / (2 * h)
    A[i, i] = -2 / h**2 + q(x[i])
    A[i, i+1] = 1 / h**2 + p(x[i]) / (2 * h)
    b[i] = f(   x[i])

A[0, 0] = 1
A[n, n] = 1
b[0] = 0
b[n] = 0

y_approx = np.linalg.solve(A, b)

y_exact_values = y_exact(x)

difference = y_approx - y_exact_values

print("x\t\t y_approx\t y_exact\t difference")
for xi, yi_approx, yi_exact, di in zip(x, y_approx, y_exact_values, difference):
    print(f"{xi:.5f}\t {yi_approx:.5f}\t {yi_exact:.5f}\t {di:.5e}")


output_file = "results_5_1.txt"
with open(output_file, "w", encoding="utf-8") as file:
    file.write("x\t\t y_приблж\t y_точное\t разница\n")
    for xi, yi_approx, yi_exact, di in zip(x, y_approx, y_exact_values, difference):
        file.write(f"{xi:.5f}\t {yi_approx:.5f}\t {yi_exact:.5f}\t {di:.5e}\n")

