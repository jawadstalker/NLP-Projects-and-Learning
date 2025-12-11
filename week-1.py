import numpy as np

A = np.array([
    [1, 2, 3],
     [4, 5, 6]
     ])

B = np.array([
    [7,  8],
     [9, 10],
     [11,12]
     ])
print(A @ B)
print(A.T)
print(B.T)

x = [1, 2, 3]
print(A @ x)


