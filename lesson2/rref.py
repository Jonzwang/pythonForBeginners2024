# import sympy
from sympy import *

M = Matrix([[1,2,3,4], [0,0,1,2], [0,0,1,0],[0,0,0,2]])
print("Matrix : {} ".format(M))
print(M.__dict__,"\n")

# Use sympy.rref() method
M_rref = M.rref()

print("The Row echelon form of matrix M and the pivot columns : {}".format(M_rref))

