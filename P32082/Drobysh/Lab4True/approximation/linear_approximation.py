from approximation.universal import *
from systems_of_equations.gauss import *


def linear_approximation_formula():
    return "Linear", "phi(x) = ax + b"


def linear_approximation_from_array(X, Y):
    X, Y = list(X).copy(), list(Y).copy()
    n = len(X)

    sum_xi = 0
    sum_xi2 = 0

    sum_yi = 0
    sum_xi_yi = 0

    for i in range(n):
        sum_xi += X[i]
        sum_xi2 += X[i] ** 2

        sum_yi += Y[i]
        sum_xi_yi += Y[i] * X[i]

    matrix_with_equations = [[sum_xi2, sum_xi, sum_xi_yi], [sum_xi, n, sum_yi]]
    gauss_answer = gauss(matrix_with_equations)
    a, b = gauss_answer

    def new_function(x):
        return a * x + b

    return True, new_function, a, b


def linear_approximation_function(a, b, h, f):
    transform = get_results_function(a, b, h, f)
    return linear_approximation_from_array(transform[0], transform[1])
