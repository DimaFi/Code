# С помощью данной таблицы функции вычислить приближенные значения функции в указанных точках, использовать интерполяционный многочлен 
# 1) в общем виде
# 2) в форме логранжа
# 3) в формне Ньютона

# 1) в общем виде

import numpy


var = 12.0

M2 = numpy.array([[0., 0., 0., 1.], [1., 1., 1., 1.], [8., 4., 2., 1.], [27., 9., 3., 1.]]) # матрица
v2 = numpy.array([var, 1+var, 8+var, 27+var]) # свободные члены

abcd = numpy.linalg.solve(M2, v2)

print(abcd)


for i in range(0, 3, 1):
    answer = abcd[0]*(i+0.5)**3 + abcd[1]*(i+0.5)**2 + abcd[2]*(i+0.5) + abcd[3]
    print(answer)