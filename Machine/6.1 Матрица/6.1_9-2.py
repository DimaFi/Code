import numpy as np

na, ma = map(int, input().split())
a = np.array([[x for x in input()] for _ in range(na)])
nb, mb = map(int, input().split())
b = np.array([[x for x in input()] for _ in range(nb)])
for i in range(4):
    if np.all(a == '.'):
        a_crop = a[0][0]
    else:
        l1, r1 = np.argmax(np.max(a == '*', axis=1)), np.argmax(np.flip(np.max(a == '*', axis=1)))
        l2, r2 = np.argmax(np.max(a == '*', axis=0)), np.argmax(np.flip(np.max(a == '*', axis=0)))
        a_crop = a[l1: a.shape[0] - r1, l2: a.shape[1] - r2]
    if np.all(b == '.'):
        b_crop = b[0][0]
    else:
        l1, r1 = np.argmax(np.max(b == '*', axis=1)), np.argmax(np.flip(np.max(b == '*', axis=1)))
        l2, r2 = np.argmax(np.max(b == '*', axis=0)), np.argmax(np.flip(np.max(b == '*', axis=0)))
        b_crop = b[l1: b.shape[0] - r1, l2: b.shape[1] - r2]
    if a_crop.shape == b_crop.shape and np.all(a_crop == b_crop):
        print("YES")
        break
    b = np.rot90(b)
else:
    print("NO")
