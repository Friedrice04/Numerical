import numpy as np
import sympy as sym


def add_rows(matrix, position, row):
    return sym.Matrix(matrix).row_insert(position, sym.Matrix(row)).tolist()


def rem_rows(matrix, position):
    return sym.Matrix(matrix).row_del(position).tolist()


def row_swap(matrix, position_a, position_b):
    tmp = matrix[position_a].copy()
    matrix[position_a] = matrix[position_b]
    matrix[position_b] = tmp

def determinant(matrix):
    return sym.mpmath.det(matrix)


#def scalar_row(matrix, i, scalar):
#    matrix[i] = list(map(lambda x: x * scalar, matrix[i]))


#def pivot(matrix, i):
#    at, max = i, matrix[i][i]
#    for j in range(i, len(matrix)):
#        val = matrix[j][i]
#        if val > max:
#            max = val
#            at = j
#
#     row_swap(matrix, i, at)
#