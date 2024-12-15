import numpy as np

V = 12
EPS = 1e-6

# Функция F(x) для уравнения
def F(x):
    return V * (4.0 / 3 * x + 1.0 / 4 * x**2 + 1.0 / 5 * x**3)

# Проверка точности y
def CheckY(x):
    return V * x

# Метод Гаусса для решения системы линейных уравнений
def gauss(sole):
    n = len(sole)
    m = len(sole[0])
    x_coords = list(range(n))
    
    for j in range(m - 1):
        mx = max(range(j, n), key=lambda i: abs(sole[i][j]))
        if abs(sole[mx][j]) < EPS:
            raise Exception("Division by zero!")
        
        sole[j], sole[mx] = sole[mx], sole[j]
        
        mx = max(range(j, m), key=lambda i: abs(sole[j][i]))
        x_coords[j], x_coords[mx] = x_coords[mx], x_coords[j]
        
        for i in range(n):
            sole[i][mx], sole[i][j] = sole[i][j], sole[i][mx]
        
        for i in range(j + 1, n):
            d = sole[i][j] / sole[j][j]
            for k in range(m):
                sole[i][k] -= sole[j][k] * d
    
    for j in range(n - 1, -1, -1):
        for i in range(j - 1, -1, -1):
            d = sole[i][j] / sole[j][j]
            sole[i][j] -= sole[j][j] * d
            sole[i][m - 1] -= sole[j][m - 1] * d
    
    result = [0] * n
    for i in range(n):
        result[x_coords[i]] = sole[i][m - 1] / sole[i][i]
    return result

# Функция для решения системы методом Гаусса с расширенной матрицей
def gauss_solve(A, B):
    for i in range(len(A)):
        A[i].append(B[i])
    return gauss(A)

# Вывод результатов
def print_results(vx, vy):
    k = 5
    for i in range(0, len(vx), k):
        m = min(i + k, len(vx))
        for j in range(i, m):
            print(f"{vx[j]:.6f}", end="\t")
        print()
        for j in range(i, m):
            print(f"{vy[j]:.6f}", end="\t")
        print()
        for j in range(i, m):
            print(f"{CheckY(vx[j]):.6f}", end="\t")
        print()
        for j in range(i, m):
            print(f"{vy[j] - CheckY(vx[j]):.6f}", end="\t")
        print()
        print()

# Метод для решения вырожденного ядра
def solve_degenerate_kernel():
    n = 3
    A = []
    for i in range(n):
        row = [1.0 / (i + j + 3) for j in range(n)]
        row[i] += 1
        A.append(row)
    
    B = [4.0 * V / 3 / (i + 3) + V / 4 / (i + 4) + V / 5 / (i + 5) for i in range(n)]
    
    vq = gauss_solve(A, B)
    
    m = 3
    l = 0
    r = 1
    h = (r - l) / (m - 1)
    vx = [l + i * h for i in range(m)]
    vy = [F(x) - sum(vq[k] * x**(k + 1) for k in range(n)) for x in vx]
    
    print_results(vx, vy)

# Квадратурный метод для решения интегрального уравнения
def solve_quadrature():
    A = 0.0
    B = 1.0
    N = 5

    def kernel(x, t):
        return x * t + x**2 * t**2 + x**3 * t**3

    def get_yt(x):
        return V * x

    # Метод численного интегрирования (квадратурный метод)
    h = (B - A) / N
    nodes = [A + i * h for i in range(N)]
    weights = [h] * N

    # Составляем систему для квадратурного метода
    matrix = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            matrix[i][j] = (1 if i == j else 0) + weights[j] * kernel(nodes[i], nodes[j])
    
    b = np.array([F(x) for x in nodes])
    y_values = np.linalg.solve(matrix, b)

    print("Узлы:")
    print(" ".join(f"{x:.10f}" for x in nodes))
    print("\nПриближенные значения y(t):")
    print(" ".join(f"{y:.10f}" for y in y_values))
    print("\nРезультаты:")
    print("t\t\ty(t)\t\tyT(t)\t\tError")
    for i in range(N):
        yT = get_yt(nodes[i])
        error = abs(y_values[i] - yT)
        print(f"{nodes[i]:.10f}\t{y_values[i]:.10f}\t{yT:.10f}\t{error:.10f}")

if __name__ == "__main__":
    print("Решение для вырожденного ядра:")
    solve_degenerate_kernel()
    print("\nРешение для квадратурного метода:")
    solve_quadrature()
