import numpy as np

def rotate_90(mat):
    return np.rot90(mat)

def get_stars_positions(matrix):
    rows, cols = np.where(matrix == '*')
    return np.array(list(zip(rows, cols)))

def match_patterns(stars_a, stars_b):
    if len(stars_a) != len(stars_b):
        return False
    
    delta = stars_b[0] - stars_a[0]
    shifted_stars_a = stars_a + delta
    
    return np.array_equal(shifted_stars_a, stars_b)

def main():
    na, ma = map(int, input().split())
    mat_a = np.array([list(input().strip()) for _ in range(na)], dtype=str)
    nb, mb = map(int, input().split())
    mat_b = np.array([list(input().strip()) for _ in range(nb)], dtype=str)
    
    # смотрим где звезды
    stars_a = get_stars_positions(mat_a)
    stars_b = get_stars_positions(mat_b)
    
    # смотрим все поворотыр
    for _ in range(4):
        if match_patterns(stars_a, stars_b):
            print("YES")
            return
        mat_b = rotate_90(mat_b)
        stars_b = get_stars_positions(mat_b)
    
    print("NO")

if __name__ == "__main__":
    main()
