from scipy.optimize import minimize_scalar

def f(x):
    return (x + 1)**2 * (x - 1) * (x - 3) - 1

def f_prime(x):
    return 4 * x**3 - 6 * x**2 - 18 * x + 2

a = -2
b = 3
epsilon = 1e-7
# Поиск максимума абсолютного значения производной на интервале [a, b]
result = minimize_scalar(lambda x: -abs(f_prime(x)), bounds=(a, b), method='bounded')
L = -result.fun  # Константа Липшица

x = (1 / (2 * L)) * (f(a) - f(b) + L * (a + b))
p = (1 / 2) * (f(a) + f(b) + L * (a - b))
delta = (1 / (2 * L)) * (f(x) - p)


while delta / (2 * L) > epsilon:
    x1, x2 = x - delta, x + delta
    p1 = (1 / 2) * (f(x1) + p)  # Значение в x1
    p2 = (1 / 2) * (f(x2) + p)  # Значение в x2

    # Выбор точки с меньшим значением функции
    if f(x1) < f(x2):
        p, x = p1, x1  # Обновляем p и x
    else:
        p, x = p2, x2  # Обновляем p и x
    # Обновляем поправку
    delta = (1 / (2 * L)) * (f(x) - p)
print(f"Минимум функции f(x) достигается в x* = {x}, f* = { f(x)}")
