import numpy as np

mat = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

def myinv(mat):
    s = np.shape(mat)
    if s[0] != s[1]:
        print("Not a square matrix!")
        return None
    elif np.linalg.det(mat) == 0.0:
        print("Determinant is zero!")
        return None
    else:
        invmat = np.linalg.inv(mat)
        print(invmat)
        return np.linalg.inv(invmat)

myinv(mat)
