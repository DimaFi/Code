 # Определение функции f(x)
def f(x):
    return (x + 1)**2 * (x - 1) * (x - 3) - 1

# Первая производная функции для нахождения параметра L
def diff(x):
    return 4 * x**3 - 6 * x**2 - 18 * x + 2

# Метод ломаных для нахождения минимума функции
def lomanye(a, b, epsilon):
    # Этап 1: инициализация параметров
    L = max(abs(diff(a)), abs(diff(b)))
    x = (1 / (2 * L)) * (f(a) - f(b) + L * (a + b))
    p = 0.5 * (f(a) + f(b) + L * (a - b))
    iter = False
    
    while True:
        # Этап 2: проверка условий и обновление
        if not iter:
            x0, p0 = x, p
        else:
            if p1 < p2:
                x0, p0 = x1, p1
            else:
                x0, p0 = x2, p2
        
        delta = (1 / (2 * L)) * (f(x0) - p0)  # Этап 3
        sigma = 2 * L * abs(delta)
        
        # Условие выхода из цикла
        if sigma <= epsilon:
            return x0, f(x0)
        
        # Этап 4: обновление точек x1 и x2
        x1 = x0 - delta
        x2 = x0 + delta
        p1 = 0.5 * (f(x1) + p0)
        p2 = 0.5 * (f(x2) + p0)
        
        iter = True

# Заданные значения для интервала и точности
a = -2
b = 3
epsilon = 1e-5

# Поиск минимума методом ломаных
x_star, f_star = lomanye(a, b, epsilon)
print(f"Минимум функции f(x) достигается в x* = {x_star}, f* = {f_star}")
