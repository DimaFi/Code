import math
import numpy as np

# Функция для задачи 1: f(x) = 3x^2 - 2x - 2 на интервале [-1, 1]
def f_task1(x):
    return 3 * x**2 - 2 * x - 2

# Функция для задачи 2: f(x) = 3x^3 + 6x^2 + x + 1 на интервале [-3, 3]
def f_task2(x):
    return x**3 + 6 * x**2 + x + 1

# Метод поразрядного поиска
def bitwise_search(a, b, f, eps=1e-9):
    delta = (b - a) / 4  # начальный шаг
    x0 = a
    f0 = f(x0)

    while abs(delta) > eps:
        x1 = x0 + delta
        f1 = f(x1)
        if f0 <= f1 or a >= x0 or x0 >= b:
            delta *= -1 / 4  # уменьшаем шаг и меняем направление
        x0, f0 = x1, f1             

    return x0, f0

# Метод дихотомии
def dichotomy_search(a, b, f, eps=1e-9):
    delta = eps 
    eps_n = 1
    while eps_n > eps:
        x1 = (a + b - delta) / 2
        x2 = (a + b + delta) / 2
        if f(x1) <= f(x2):
            b = x2
        else:
            a = x1
        eps_n = (b - a) / 2

    x_min = (a + b) / 2
    f_min = f(x_min)
    return x_min, f_min

# Метод золотого сечения
def golden_section_search(a, b, f, eps=1e-6):
    tau = (np.sqrt(5) - 1) / 2  # коэффициент золотого сечения
    x1 = a + (3 - np.sqrt(5)) / 2 * (b - a)
    x2 = a + (np.sqrt(5) - 1) / 2 * (b - a)
    f1, f2 = f(x1), f(x2)

    while (b - a) / 2 > eps:
        if f1 <= f2:
            b, x2, f2 = x2, x1, f1
            x1 = b - tau * (b - a)
            f1 = f(x1)
        else:
            a, x1, f1 = x1, x2, f2
            x2 = a + tau * (b - a)
            f2 = f(x2)

    x_min = (a + b) / 2
    f_min = f(x_min)
    return x_min, f_min

# Метод параболической аппроксимации
def parabola_search(a, b, f, eps=1e-6):
    x1, x2, x3 = a, (a + b) / 2, b
    f1, f2, f3 = f(x1), f(x2), f(x3)

    a0, a1 = f1, (f2 - f1) / (x2 - x1)
    a2 = 1 / (x3 - x2) * ((f3 - f1) / (x3 - x1) - (f2 - f1) / (x2 - x1))
    x_min = 1 / 2 * (x1 + x2 - a1 / a2)
    f_min = f(x_min)
    delta = 1

    while abs(delta) > eps:
        delta = x_min
        if f_min < f2:
            x1, x2, x3 = x2, x_min, x3
            f1, f2, f3 = f2, f_min, f3
        else:
            x1, x2, x3 = x1, x_min, x2
            f1, f2, f3 = f1, f_min, f2

        a0, a1 = f1, (f2 - f1) / (x2 - x1)
        a2 = 1 / (x3 - x2) * ((f3 - f1) / (x3 - x1) - (f2 - f1) / (x2 - x1))
        x_min = 1 / 2 * (x1 + x2 - a1 / a2)
        f_min = f(x_min)
        delta -= x_min

    return x_min, f_min

if __name__ == "__main__":
    # Задание 1: Минимизация f(x) = 3x^2 - 2x - 2 на интервале [-1, 1]
    print("Задание 1: Минимизация f(x) = 3x^2 - 2x - 2 на интервале [-1, 1]")

    # Метод поразрядного поиска
    x_min, f_min = bitwise_search(-1, 1, f_task1)
    print(f"Метод поразрядного поиска: x = {x_min}, f(x) = {f_min}")

    # Метод дихотомии
    x_min, f_min = dichotomy_search(-1, 1, f_task1)
    print(f"Метод дихотомии: x = {x_min}, f(x) = {f_min}")

    # Метод золотого сечения
    x_min, f_min = golden_section_search(-1, 1, f_task1)
    print(f"Метод золотого сечения: x = {x_min}, f(x) = {f_min}")

    # Задание 2: Минимизация f(x) = 3x^3 + 6x^2 + x + 1 на интервале [-3, 3]
    print("\nЗадание 2: Минимизация f(x) = 3x^3 + 6x^2 + x + 1 на интервале [-3, 3]")

    # Метод параболической аппроксимации
    x_min, f_min = parabola_search(-3, 3, f_task2)
    print(f"Метод параболической аппроксимации: x = {x_min}, f(x) = {f_min}")
