import numpy as np

x = np.array([0, 1, 2, 3])
V = 12.0
y = np.array([V, 1 + V, 8 + V, 27 + V])

def lagrange(x, y, x_values):
    n = len(x)
    result = []
    for x_val in x_values:
        L_n = 0
        for i in range(n):
            l_i = 1
            for j in range(n):
                if i != j:
                    l_i *= (x_val - x[j]) / (x[i] - x[j])
            L_n += l_i * y[i]
        result.append(L_n)
    return result

x_value = [0.5, 1.5, 2.5]

interpolated_values = lagrange(x, y, x_value)

for x_val, y_val in zip(x_value, interpolated_values):
    print(f"x = {x_val}: y = {y_val}")