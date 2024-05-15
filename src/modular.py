import sympy as sym
import numpy as np


def modular_inv(matrix, mod):
    q, r = sym.Matrix(matrix).QRdecomposition()
    res = q.inv_mod(mod) #* r.inv_mod(mod)

    return res


def solve_modular(matrix_a, matrix_b, mod):
    matrix_a = sym.Matrix(matrix_a)
    pass
    #q, r = sym.Matrix(matrix_a).QRdecomposition()
#
 #   prod = modular_inv(r.tolist(), mod) * q.transpose() * sym.Matrix(matrix_b)
#
 #   return np.array(prod.tolist())
    # r*x = q^(-1)*matrix_b mod (mod)
    # r upper triangular
  #  for k in range(matrix_a. - 1):
  #      entry_value = self._arr[k][k]
  #      for i in range(k + 1, self._row_num):
  #          c = (self._arr[i][k] * self.find_mod_inverse(int(entry_value), mod)) % mod
  #          self._row_add_row_mod(i, k, -c, mod)


