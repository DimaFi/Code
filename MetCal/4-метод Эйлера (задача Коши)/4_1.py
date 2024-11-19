import numpy as np

V = 12.0

def f(x, y):
    return 4 * (x**3) - 3 * (x**2) * V

def exact_solution(x):
    return (x**3) * (x -V)

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

# Улучшенный метод Эйлера
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

x0 = V
y0 = 0
x_end = V + 5

steps = [1, 0.1, 0.05]

for h in steps:
    print(f"\nШаг h = {h}")
    
    # Метод Эйлера
    x_euler, y_euler = euler_method(f, x0, y0, h, x_end)
    print("Метод Эйлера:")
    print("x\t\tПриближенное y\tТочное y\t\tРазница")
    for x_val, y_val in zip(x_euler, y_euler):
        y_exact = exact_solution(x_val)
        diff = y_val - y_exact
        print(f"{x_val:.5f}\t{y_val:.5f}\t{y_exact:.5f}\t{diff:.5f}")
    
    # Улучшенный метод Эйлера
    x_improved, y_improved = improved_euler_method(f, x0, y0, h, x_end)
    print("\nУлучшенный метод Эйлера:")
    print("x\t\tПриближенное y\tТочное y\t\tРазница")
    for x_val, y_val in zip(x_improved, y_improved):
        y_exact = exact_solution(x_val)
        diff = y_val - y_exact
        print(f"{x_val:.5f}\t{y_val:.5f}\t{y_exact:.5f}\t{diff:.5f}")


# Открываем файл для записи
with open("results_4_1.txt", "w", encoding="utf-8") as file:
    for h in steps:
        file.write(f"\nШаг h = {h}\n")
        print(f"\nШаг h = {h}")
        
        # Метод Эйлера
        x_euler, y_euler = euler_method(f, x0, y0, h, x_end)
        file.write("Метод Эйлера:\n")
        file.write("x\t\tПриближенное y\tТочное y\t\tРазница\n")
        print("Метод Эйлера:")
        print("x\t\tПриближенное y\tТочное y\t\tРазница")
        for x_val, y_val in zip(x_euler, y_euler):
            y_exact = exact_solution(x_val)
            diff = y_val - y_exact
            file.write(f"{x_val:.5f}\t{y_val:.5f}\t{y_exact:.5f}\t{diff:.5f}\n")
            print(f"{x_val:.5f}\t{y_val:.5f}\t{y_exact:.5f}\t{diff:.5f}")
        
        # Улучшенный метод Эйлера
        x_improved, y_improved = improved_euler_method(f, x0, y0, h, x_end)
        file.write("\nУлучшенный метод Эйлера:\n")
        file.write("x\t\tПриближенное y\tТочное y\t\tРазница\n")
        print("\nУлучшенный метод Эйлера:")
        print("x\t\tПриближенное y\tТочное y\t\tРазница")
        for x_val, y_val in zip(x_improved, y_improved):
            y_exact = exact_solution(x_val)
            diff = y_val - y_exact
            file.write(f"{x_val:.5f}\t{y_val:.5f}\t{y_exact:.5f}\t{diff:.5f}\n")
            print(f"{x_val:.5f}\t{y_val:.5f}\t{y_exact:.5f}\t{diff:.5f}")