import numpy as np
import scipy as sc


# given n points each with x,y values
# Input x values in 'a' and y values in 'b'
def vandermonde(x, fx, degree):
    """
    Generate a vandermonde polynomial using x and f(x) arrays of values
    @param degree: degree of polynomial to be generated (uses first 'degree' values)
    @param x: x values
    @param fx: f(x) values
    @return:
    """

    v = np.vander(x[:degree+1], degree+1)
    print(v)
    ans = np.linalg.solve(v, fx[:degree+1])
    return ans


def lagrangian(x, fx, degree):
    """

    @param x: x values
    @param fx: f(x) values
    @return:
    """
    return sc.interpolate.lagrange(x[:degree+1], fx[:degree+1])


def newton_coefficient(x_data, y_data, degree):
    """
    x: list or np array contanining x data points
    y: list or np array contanining y data points
    """

    new_x = np.copy(x_data[:degree + 1])
    new_y = np.copy(y_data[:degree + 1])
    for i in range(1, degree+1):
        enum = (new_y[i:degree+1] - new_y[i - 1])
        denom = (new_x[i:degree + 1] - new_x[i - 1])
        new_y[i:degree+1] = enum/denom

    return new_y


def newton_polynomial(x_data, y_data, degree, x):
    """
    x_data: data points at x
    y_data: data points at y
    x: evaluation point(s)
    """
    a = newton_coefficient(x_data, y_data, degree)
    n = len(x_data) - 1  # Degree of polynomial
    p = a[n]

    for k in range(1, n + 1):
        p = a[n - k] + (x - x_data[n - k])*p

    return p


def taylor(function, around, degree):
    return sc.interpolate.approximate_taylor_polynomial(function, around, degree, 1)