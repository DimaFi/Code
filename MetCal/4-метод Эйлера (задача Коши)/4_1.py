import numpy as np

# Параметр V
V = 12.0

# Определяем правую часть уравнения
def f(x, y):
    return x**3 * (x - V)

# Метод Эйлера
def euler_method(f, x0, y0, h, x_end):
    x_values = [x0]
    y_values = [y0]
    
    x = x0
    y = y0
    while x < x_end:
        y += h * f(x, y)
        x += h
        x_values.append(x)
        y_values.append(y)
    
    return np.array(x_values), np.array(y_values)

# Улучшенный метод Эйлера (метод Хойна)
def improved_euler_method(f, x0, y0, h, x_end):
    x_values = [x0]
    y_values = [y0]
    
    x = x0
    y = y0
    while x < x_end:
        y_predict = y + h * f(x, y)
        y += (h / 2) * (f(x, y) + f(x + h, y_predict))
        x += h
        x_values.append(x)
        y_values.append(y)
    
    return np.array(x_values), np.array(y_values)

# Параметры задачи
x0 = V
y0 = 0
x_end = V + 5

# Шаги h
steps = [1, 0.1, 0.05]

# Вычисление и вывод результатов для каждого шага
for h in steps:
    print(f"\nШаг h = {h}")
    
    # Метод Эйлера
    x_euler, y_euler = euler_method(f, x0, y0, h, x_end)
    print("Метод Эйлера:")
    print("x\t\tПриближенное y")
    for x_val, y_val in zip(x_euler, y_euler):
        print(f"{x_val:.5f}\t{y_val:.5f}")
    
    # Улучшенный метод Эйлера
    x_improved, y_improved = improved_euler_method(f, x0, y0, h, x_end)
    print("\nУлучшенный метод Эйлера:")
    print("x\t\tПриближенное y")
    for x_val, y_val in zip(x_improved, y_improved):
        print(f"{x_val:.5f}\t{y_val:.5f}")
