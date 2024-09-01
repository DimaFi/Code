import numpy as np

V = 12
EPS = 1e-6

def F(x):
    return V * (4.0 / 3 * x + 1.0 / 4 * x**2 + 1.0 / 5 * x**3)

def CheckY(x):
    return V * x

def Gauss(sole):
    n = len(sole)
    m = len(sole[0])
    x_coords = list(range(n))

    for j in range(m - 1):
        mx = max(range(j, n), key=lambda i: abs(sole[i][j]))
        if abs(sole[mx][j]) < EPS:
            raise Exception("Division by zero!")

        # Swap rows
        sole[j], sole[mx] = sole[mx], sole[j]
        x_coords[j], x_coords[mx] = x_coords[mx], x_coords[j]

        # Find max in row
        mx = max(range(j, m), key=lambda i: abs(sole[j][i]))
        for i in range(n):
            sole[i][mx], sole[i][j] = sole[i][j], sole[i][mx]

        # Eliminate
        for i in range(j + 1, n):
            d = sole[i][j] / sole[j][j]
            for k in range(m):
                sole[i][k] -= sole[j][k] * d

    # Back substitution
    for j in range(n - 1, -1, -1):
        for i in range(j - 1, -1, -1):
            d = sole[i][j] / sole[j][j]
            sole[i][j] -= sole[j][j] * d
            sole[i][m - 1] -= sole[j][m - 1] * d

    # Extract solution
    result = [0] * n
    for i in range(n):
        result[x_coords[i]] = sole[i][m - 1] / sole[i][i]
    
    return result

def GaussSolve(A, B):
    for i in range(len(A)):
        A[i].append(B[i])
    return Gauss(A)

def PrintResults(vx, vy):
    k = 5
    for i in range(0, len(vx), k):
        m = min(i + k, len(vx))
        # Print vx
        print("\t".join(f"{vx[j]:.6f}" for j in range(i, m)))
        # Print vy
        print("\t".join(f"{vy[j]:.6f}" for j in range(i, m)))
        # Print check_y
        print("\t".join(f"{CheckY(vx[j]):.6f}" for j in range(i, m)))
        # Print deviations
        print("\t".join(f"{vy[j] - CheckY(vx[j]):.6f}" for j in range(i, m)))
        print()

def Solve():
    n = 3
    A = []
    for i in range(n):
        row = [(1.0 / (i + j + 3)) for j in range(n)]
        row[i] += 1
        A.append(row)
    
    B = [4.0 * V / 3 / (i + 3) + V / 4 / (i + 4) + V / 5 / (i + 5) for i in range(n)]
    vq = GaussSolve(A, B)
    
    m = 3
    l = 0
    r = 1
    h = (r - l) / (m - 1)
    vx = [l + i * h for i in range(m)]
    vy = [F(x) - sum(vq[k] * x**(k + 1) for k in range(len(vq))) for x in vx]
    
    PrintResults(vx, vy)

if __name__ == "__main__":
    Solve()
