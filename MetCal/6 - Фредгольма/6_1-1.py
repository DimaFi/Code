import numpy as np
import matplotlib.pyplot as plt

def g(x):
    return 1 + x

def h(t):
    return 1 - t

def f(x):
    return x * np.exp(-x)

# методом трапеции ищем площадь под кривой
def numerical_integral(func, a, b, n):
    x = np.linspace(a, b, n)
    dx = (b - a) / (n - 1)
    return np.trapz(func(x), x)  # Метод трапеций

# найдя все x можно подставить в уравнение
def solve_integral_equation(a, b, n):
    # Дискретизация интервала [a, b]
    x_values = np.linspace(a, b, n)
    
    # Строим правую часть уравнения
    integral_value = numerical_integral(h, a, b, n)  # Интеграл по t для фиксированного x
    f_values = f(x_values)
    
    y_values = np.array([f_values[i] / (g(x_values[i]) * integral_value) for i in range(n)])
    
    return x_values, y_values

a = 0  # Левая граница
b = 1  # Правая граница
n = 100  # Количество точек дискретизации

x_values, y_values = solve_integral_equation(a, b, n)

plt.plot(x_values, y_values, label="Решение y(x)")
plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("Решение интегрального уравнения Фредгольма с вырожденным ядром")
plt.legend()
plt.grid(True)
plt.show()
