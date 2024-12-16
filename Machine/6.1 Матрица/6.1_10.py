import sys

def determinant(matrix, n):
    """опред матрицы методом Гаусса."""
    det = 1
    for i in range(n):
        # Ищем строку с максимальным элементом в текущем столбце для предотвращения деления на ноль
        max_row = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > abs(matrix[max_row][i]):
                max_row = j
        
        # Меняем строки местами, если нужно
        if max_row != i:
            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
            det *= -1  # При обмене строк знак определителя меняется
        
        # Если главный элемент матрицы на текущей строке равен нулю, то определитель равен нулю
        if matrix[i][i] == 0:
            return 0
        
        # Преобразуем матрицу, делая все элементы под главной диагональю равными нулю
        for j in range(i + 1, n):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, n):
                matrix[j][k] -= factor * matrix[i][k]
    
    # опред — это произведение элементов на главной диагонали
    for i in range(n):
        det *= matrix[i][i]
    
    return det

def main():
    n = int(input())  # Читаем размерность матрицы
    matrix = []
    
    for i in range(n):
        matrix.append(list(map(float, input().split())))
    
    result = determinant(matrix, n)
    
    print(f"{result:.8f}")

if __name__ == "__main__":
    main()
