import math

# Define the function f(x) and its derivatives
def f(x):
    return math.cos(5 * x) - math.sin(2 * x)

def diff1(x):
    return -5 * math.sin(5 * x) - 2 * math.cos(2 * x)

def diff2(x):
    return -25 * math.cos(5 * x) + 4 * math.sin(2 * x)

# Midpoint method
def midpoint_method(a, b, epsilon):
    while True:
        x_min = (a + b) / 2
        if abs(diff1(x_min)) <= epsilon:
            return x_min, f(x_min)
        if diff1(x_min) > 0:
            b = x_min # если взрастает то минимум слева
        else:
            a = x_min # если убывает то справа

# Chord method
def chord_method(a, b, epsilon):
    diff_a = diff1(a)
    diff_b = diff1(b)
    while True:
        x_min = a - (diff_a / (diff_a - diff_b)) * (a - b)
        if abs(diff1(x_min)) <= epsilon:
            return x_min, f(x_min)
        if diff1(x_min) > 0:
            b = x_min
        else:
            a = x_min

# Newton's method
def newton_method(x0, epsilon):
    xk = x0
    while True:
        xk1 = xk - (diff1(xk) / diff2(xk))
        print(xk)
        if abs(diff1(xk1)) <= epsilon:
            return xk1, f(xk1)
        xk = xk1

# Parameters        
a = 0.0
b = 1.0 
x0 = 0.5
epsilon = 1e-5

# Calculate minima using each method
x_star_mid, f_star_mid = midpoint_method(a, b, epsilon)
x_star_chord, f_star_chord = chord_method(a, b, epsilon)
x_star_newton, f_star_newton = newton_method(x0, epsilon)

# Output results
print(f"Midpoint Method: Minimum at x* = {x_star_mid}, f* = {f_star_mid}")
print(f"Chord Method: Minimum at x* = {x_star_chord}, f* = {f_star_chord}")
print(f"Newton's Method: Minimum at x* = {x_star_newton}, f* = {f_star_newton}")
