def replace_even_elements_with_zeros(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] % 2 == 0:
                matrix[i][j] = 0

n, m = map(int, input().split())
matrix_a = [list(map(int, input().split())) for _ in range(n)]
matrix_b = [list(map(int, input().split())) for _ in range(n)]

replace_even_elements_with_zeros(matrix_a)
replace_even_elements_with_zeros(matrix_b)

if matrix_a == matrix_b:
    print("YES")
else:
    print("NO")
