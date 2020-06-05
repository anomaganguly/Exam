#Q9. Singular Value Decomposition of a Matrix

import numpy as np
import time

np.set_printoptions(precision = 4)
np.set_printoptions(suppress = True)

a = np.array([[2.0, 1.0], [1.0, 0.0], [0.0, 1.0]]) #Initialising matrix A
b = np.array([[1.0, 1.0, 0.0], [1.0, 0.0, 1.0], [0.0, 1.0, 1.0]]) #Initialising matrix B

u1, s1, vf1 = np.linalg.svd(a) # Using the numpy built-in fn to do SVD
u2, s2, vf2 = np.linalg.svd(b)

print("Singular values of first matrix are:\n\n", s1)
print("\nSingular values of second matrix are:\n\n", s2)