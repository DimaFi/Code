import numpy as np

def main():
    n = int(input())
    matrix = []
    
    for i in range(n):
        matrix.append(list(map(float, input().split())))
    
    np_matrix = np.array(matrix)
    
    # определитель
    result = np.linalg.det(np_matrix)
    
    print(f"{result:.8f}")

if __name__ == "__main__":
    main()
