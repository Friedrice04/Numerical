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
    ans = np.linalg.solve(v, fx[:degree+1])
    return ans


def lagrangian(x, fx, degree):
    """

    @param x: x values
    @param fx: f(x) values
    @return:
    """
    return sc.interpolate.lagrange(x[:degree+1], fx[:degree+1])


def poly_newton_coefficient(x, y, degree):
    """
    x: list or np array contanining x data points
    y: list or np array contanining y data points
    """

    x = np.copy(x[:degree+1])
    a = np.copy(y[:degree+1])
    for k in range(1, degree+1):
        a[k:degree+1] = (a[k:degree+1] - a[k - 1])/(x[k:degree+1] - x[k - 1])

    return a


def newton_polynomial(x_data, y_data, x):
    """
    x_data: data points at x
    y_data: data points at y
    x: evaluation point(s)
    """
    a = poly_newton_coefficient(x_data, y_data)
    n = len(x_data) - 1  # Degree of polynomial
    p = a[n]

    for k in range(1, n + 1):
        p = a[n - k] + (x - x_data[n - k])*p

    return p