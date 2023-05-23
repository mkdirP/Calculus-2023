from approximation.universal import *
from systems_of_equations.gauss import *


def exponential_approximation_formula():
    return "Exponential", "phi(x) = ae^{bx}"


def exponential_approximation_from_array(X, Y):
    X, Y = list(X).copy(), list(Y).copy()
    n = len(X)

    sum_xi = 0
    sum_xi2 = 0

    sum_yi = 0
    sum_xi_yi = 0

    for i in range(n):
        if Y[i] <= 0:
            return False, False
        sum_xi += X[i]
        sum_xi2 += X[i] ** 2

        sum_yi += ln(Y[i])
        sum_xi_yi += X[i] * ln(Y[i])
    matrix_with_equations = [[sum_xi2, sum_xi, sum_xi_yi], [sum_xi, n, sum_yi]]
    gauss_answer = gauss(matrix_with_equations)
    a, b = math.e ** gauss_answer[1], gauss_answer[0]

    def new_function(x):
        return a * math.e**(b * x)

    return True, new_function, a, b


def exponential_approximation_function(a, b, h, f):
    transfer = get_results_function(a, b, h, f)
    return exponential_approximation_from_array(transfer[0], transfer[1])
