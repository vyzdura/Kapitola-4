import numpy as np

mat = np.array([
    [2, 6, 3, 9, 9, 3, 3, 8, 8, 4, 9, 1],
    [7, 1, 7, 3, 9, 8, 5, 8, 1, 1, 3, 9],
    [9, 4, 3, 2, 3, 8, 4, 8, 9, 5, 4, 3],
    [3, 6, 5, 7, 3, 8, 8, 8, 6, 7, 4, 10],
    [5, 7, 5, 9, 4, 3, 2, 2, 5, 2, 4, 8],
    [3, 1, 10, 5, 4, 3, 4, 5, 4, 7, 8, 7],
    [5, 10, 1, 6, 4, 9, 9, 2, 4, 6, 3, 5],
    [3, 6, 4, 3, 7, 8, 5, 5, 6, 6, 9, 3],
    [1, 8, 4, 2, 9, 8, 1, 6, 6, 4, 6, 8],
    [9, 8, 1, 4, 9, 9, 8, 4, 4, 9, 6, 2],
    [3, 7, 7, 1, 9, 3, 8, 5, 1, 6, 4, 1],
    [7, 4, 10, 4, 5, 8, 7, 7, 3, 1, 6, 5]
])

def myinv(mat):
    s = np.shape(mat)
    if s[0] != s[1]:
        print("Not a square matrix!")
        return None
    elif np.linalg.det(mat) == 0.0:
        print("Determinant is zero!")
        return None
    elif s[0] > 10 and s[1] > 10:
        print('matrix rank is greater than 10!')
    else:
        invmat = np.linalg.inv(mat)
        print(invmat)
        return np.linalg.inv(invmat)

myinv(mat)
