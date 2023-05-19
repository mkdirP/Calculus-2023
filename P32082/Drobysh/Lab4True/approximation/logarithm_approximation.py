from approximation.universal import *
from systems_of_equations.gauss import *


def logarithm_approximation_formula():
    return "Logarithm", "phi(x) = ae^{bx}"


def logarithm_approximation_from_array(X, Y):
    X, Y = list(X).copy(), list(Y).copy()
    n = len(X)

    sum_xi = 0
    sum_xi2 = 0

    sum_yi = 0
    sum_xi_yi = 0

    for i in range(n):
        if X[i] <= 0:
            return False, False
        sum_xi += ln(X[i])
        sum_xi2 += ln(X[i]) ** 2

        sum_yi += Y[i]
        sum_xi_yi += ln(X[i]) * Y[i]
    matrix_with_equations = [[sum_xi2, sum_xi, sum_xi_yi], [sum_xi, n, sum_yi]]
    gauss_answer = gauss(matrix_with_equations)
    a, b = gauss_answer

    def new_function(x):
        return a * ln(x) + b

    return True, new_function, a, b


def logarithm_approximation_function(a, b, h, f):
    transfer = get_results_function(a, b, h, f)
    return logarithm_approximation_from_array(transfer[0], transfer[1])
