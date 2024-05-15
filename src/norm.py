import mpmath
import numpy as np
import sympy as sym


def frobenius_norm(A):
    A = sym.Matrix(A)
    return mpmath.mnorm(A, p='f')


def inf_norm(A):
    A = sym.Matrix(A)
    return mpmath.mnorm(A, p='inf')


def norm_1(A):
    A = sym.Matrix(A)
    return mpmath.mnorm(A, p='1')
