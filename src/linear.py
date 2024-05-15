import mpmath
import numpy as np
import scipy as sp
import sympy as sym
from src.interpolation import taylor

# LU decomp
# Cholesky
#


def lin_solve(matrix_a, matrix_b):
    return np.linalg.solve(matrix_a, matrix_b)


def lu_solve(matrix_a, matrix_b):
    return mpmath.lu_solve(matrix_a, matrix_b)

def cholesky_solve(matrix_a, matrix_b):
    return mpmath.cholesky_solve(matrix_a, matrix_b)


def roots(function, near, degree_taylor=5):
    poly = taylor(function, near, degree_taylor)
    return np.roots(poly)

