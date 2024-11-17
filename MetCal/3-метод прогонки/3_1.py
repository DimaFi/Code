import numpy as np

n = 5
V = 4

a = np.array([(V + i) / 100 for i in range(1, n)])  # поддиагонал
b_diagonal = np.array([V + i for i in range(0, n)])  # главная диагональ
c = np.array([(V + i) / 100 for i in range(2, n + 1)])  # наддиагональ

A = np.zeros((n, n))
np.fill_diagonal(A, b_diagonal)
np.fill_diagonal(A[1:], a)
np.fill_diagonal(A[:, 1:], c)

b = A @ b_diagonal  # умножаем матрицу A на столбец главной диагонали b_diagonal

# метод прогонки

def progonka(a, b, c, d):
    n = len(d)
    P = np.zeros(n-1)
    Q = np.zeros(n)

    # Прямой ход
    P[0] = c[0] / b[0]
    Q[0] = d[0] / b[0]
    for i in range(1, n-1):
        denominator = b[i] - a[i-1] * P[i-1] #  это знаменатель в формулах для P и Q
        # Он учитывает предыдущие коэффициенты, что позволяет нам исключить неизвестные из предыдущих уравнений
        
        P[i] = c[i] / denominator # исп для того, чтобы "исключить" одно из неизвестных при переходе от одного уравнения к следующему
        Q[i] = (d[i] - a[i-1] * Q[i-1]) / denominator # показывает, что происходит с текущим уравнением после учета влияния всех предыдущих уравнений
        
    # находим последний элемент
    Q[-1] = (d[-1] - a[-2] * Q[-2]) / (b[-1] - a[-2] * P[-2])

    # обратный ход, начинаем с конца системы
    x = np.zeros(n)
    x[-1] = Q[-1]   
    for i in range(n-2, -1, -1):
        x[i] = Q[i] - P[i] * x[i+1]

    return x, P, Q

x, P, Q = progonka(a, b_diagonal, c, b)

print("Матрица A:")
print(A)
print("\nВектор правой части b = A * (столбец главной диагонали):")
print(b)
print("\nПрогоночные коэффициенты P_i:")
print(P)
print("\nПрогоночные коэффициенты Q_i:")
print(Q)
print("\nРешение системы (вектор x):")
print(x)
