import matplotlib.pyplot as plt
import math

import numpy as np
import scipy as sp
import scipy.linalg
from src.differentiation import *
from src.interpolation import *
from src.matrix import *
from src.non_linear import *
from src.linear import *
from src.modular import *
import numdifftools as nd
from src.norm import *


def poly_graph(x_data, y_data, degree):
    plt.scatter(x_data, y_data, label='data')
    x = np.linspace(int(x_data[0]), int(x_data[degree]), 100)
    func = vandermonde(x_data, y_data, degree)[::-1]
    fx = np.polynomial.polynomial.polyval(x, func)
    plt.plot(x, fx, label='Polynomial')
    plt.legend()
    plt.show()


def function(x):
    return np.exp(x-1) - np.power(x, 3) - 2


before =   [[0, 2, 1, 0, 0, 0, 2, 0, 0, 0, 28717],
            [0, 1, 0, 2, 0, 0, 1, 0, 0, 0, 2612],
            [0, 3, 2, 0, 0, 1, 0, 0, 0, 0, 2371],
            [0, 0, 3, 0, 1, 0, 1, 0, 0, 0, 11957],
            [0, 1, 0, 3, 1, 0, 0, 0, 0, 0, 8368],
            [3, 0, 0, 0, 0, 0, 1, 1, 0, 0, 9978],
            [2, 1, 0, 0, 0, 0, 0, 0, 1, 0, 9203],
            [0, 2, 1, 1, 0, 0, 0, 0, 0, 0, 11275],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 9257],
            [0, 5, 0, 1, 0, 0, 0, 0, 0, 0, 30226],
            [0, 1, 2, 0, 1, 0, 0, 0, 1, 0, 4885],
            [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 22566],
            [0, 1, 1, 2, 0, 0, 0, 1, 0, 0, 2468],
            [0, 0, 2, 0, 1, 0, 0, 0, 1, 0, 11513],
            [2, 2, 2, 0, 0, 1, 0, 0, 0, 0, 23705],
            [5, 0, 2, 0, 0, 0, 0, 1, 0, 0, 11874],
            [2, 1, 1, 0, 1, 0, 0, 0, 1, 0, 32110],
            [0, 0, 0, 1, 0, 1, 2, 0, 0, 0, 7255],
            [2, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1245],
            [1, 0, 2, 2, 0, 0, 0, 0, 0, 0, 3783],
            [1, 3, 1, 1, 0, 0, 0, 0, 0, 0, 12000],
            [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 7607],
            [0, 3, 2, 0, 0, 0, 0, 0, 0, 1, 8637]]


#mat_a = np.array(before)[:, :10]

mat_b = np.array(before)[:, 10:]

mat_a = np.array([[2, 3, 1, 1],
                  [1, 2, 3, 1],
                  [1, 1, 2, 3],
                  [3, 1, 1, 2]])
ident = np.identity(4)
def main():
    print(roots(function, -2))
    #print(np.linalg.matrix_power(ident + np.divide(frobenius_norm(mat_a), 1000000), 1000000))
    #print(sym.Matrix(mat_a).inv())
    #print(solve_modular(mat_a, mat_b, 17))
    #print(chinese_remainder(m, a))  # Co
    #print(taylor(function, 0, 4))

if __name__ == "__main__":
    main()
