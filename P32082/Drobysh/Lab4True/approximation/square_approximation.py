from approximation.universal import *
from systems_of_equations.gauss import *


def square_approximation_formula():
    return "Square", "phi(x) = a_2 * x^2 + a_1 * x + a_0"


def square_approximation_from_array(X, Y):
    X, Y = list(X).copy(), list(Y).copy()
    n = len(X)

    sum_xi = 0
    sum_xi2 = 0
    sum_xi3 = 0
    sum_xi4 = 0

    sum_yi = 0
    sum_xi_yi = 0
    sum_xi2_yi = 0

    for i in range(n):
        sum_xi += X[i]
        sum_xi2 += X[i] ** 2
        sum_xi3 += X[i] ** 3
        sum_xi4 += X[i] ** 4

        sum_yi += Y[i]
        sum_xi_yi += X[i] * Y[i]
        sum_xi2_yi += X[i] ** 2 * Y[i]

    matrix_of_equations = [[sum_xi3, sum_xi2, sum_xi, sum_xi_yi], [sum_xi4, sum_xi3, sum_xi2, sum_xi2_yi],
                           [sum_xi2, sum_xi, n, sum_yi]]
    gauss_answer = gauss(matrix_of_equations)

    a, b, c = gauss_answer

    def new_function(x):
        return a * x ** 2 + b * x + c

    return True, new_function, a, b, c


def square_approximation_function(a, b, h, f):
    transform = get_results_function(a, b, h, f)
    return square_approximation_from_array(transform[0], transform[1])
