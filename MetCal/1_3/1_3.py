# from numpy import arange
from math import prod

def NetRec(y_i, x_i, xs, xe):
    if xs == xe:
        return y_i[xs]
    else:
        a = (NetRec(y_i,x_i,xs+1,xe)-NetRec(y_i,x_i,xs,xe-1))/(xe-xs)
        print(f"{xs}, {xe}", a)
        return a
    
def main():
    variant, n = int(input()), int(input())
    y_i = [variant + i**3 for i in range(0,n+1)] # значения функции в углах интерполяции
    x_i = [i for i in range(0,n)] # узлы интерполяции (переменная Х)
    for x in [0.5 + i for i in range(0, 3)]:  
        answer = sum([NetRec(y_i,x_i,0,i)*prod([x-i1 for i1 in range(0,i)]) for i in range(0,n)])
        print(f"P_n({x}) = {answer}")
    

main()
