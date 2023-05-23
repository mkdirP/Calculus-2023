import math
from scipy.misc import derivative
import numpy as np


def simple_iteration_method(equation, a, b, accuracy, max_iterations):
    max_derivative = abs(derivative(equation, a, n=1))
    for i in np.arange(a, b, accuracy):
        if max_derivative < abs(derivative(equation, i, n=1)):
            max_derivative = abs(derivative(equation, i, n=1))
    l = -1 / max_derivative
    phi_f = lambda x: l * equation(x) + x
    iterations = 0
    q = abs(derivative(phi_f, a, n=1))
    for i in np.arange(a, b, accuracy):
        if abs(derivative(phi_f, i, n=1)) > q:
            q = abs(derivative(phi_f, i, n=1))
    if q >= 1:
        print("The convergence condition is not met")
        return None, None
    x_prev = a
    x = phi_f(a)
    while (iterations < max_iterations) and abs(x - x_prev) >= accuracy:
        iterations += 1
        buf = x
        x = phi_f(x_prev)
        x_prev = buf
    return x, iterations
