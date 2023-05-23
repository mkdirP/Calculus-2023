from approximation.universal import *
from systems_of_equations.gauss import *


def cube_approximation_formula():
    return "Cube", "phi(x) = a_2 * x^2 + a_1 * x + a_0"


def cube_approximation_from_array(X, Y):
    X, Y = list(X).copy(), list(Y).copy()
    n = len(X)

    sum_xi = 0
    sum_xi2 = 0
    sum_xi3 = 0
    sum_xi4 = 0
    sum_xi5 = 0
    sum_xi6 = 0

    sum_yi = 0
    sum_xi_yi = 0
    sum_xi2_yi = 0
    sum_xi3_yi = 0

    for i in range(n):
        sum_xi += X[i]
        sum_xi2 += X[i] ** 2
        sum_xi3 += X[i] ** 3
        sum_xi4 += X[i] ** 4
        sum_xi5 += X[i] ** 5
        sum_xi6 += X[i] ** 6

        sum_yi += Y[i]
        sum_xi_yi += X[i] * Y[i]
        sum_xi2_yi += X[i] ** 2 * Y[i]
        sum_xi3_yi += X[i] ** 3 * Y[i]
    matrix_with_equations = [[sum_xi6, sum_xi5, sum_xi4, sum_xi3, sum_xi3_yi],
                             [sum_xi5, sum_xi4, sum_xi3, sum_xi2, sum_xi2_yi],
                             [sum_xi4, sum_xi3, sum_xi2, sum_xi, sum_xi_yi], [sum_xi3, sum_xi2, sum_xi, n, sum_yi]]
    gauss_answer = gauss(matrix_with_equations)
    a, b, c, d = gauss_answer

    def new_function(x):
        return a * x ** 3 + b * x ** 2 + c * x + d

    return True, new_function, a, b, c, d


def cube_approximation_function(a, b, h, f):
    transform = get_results_function(a, b, h, f)
    return cube_approximation_from_array(transform[0], transform[1])
