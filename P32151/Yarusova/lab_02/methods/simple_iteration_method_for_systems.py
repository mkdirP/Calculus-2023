import numpy as np
from scipy.misc import derivative
from sympy import *

x, y = symbols('x y')

phi = {
    1: (4 - y ** 2) ** (1 / 2),
    2: x ** 2,
    3: 0.3 - 0.1 * x ** 2 - 0.2 * y ** 2,
    4: 0.7 - 0.2 * x ** 2 - 0.1 * x * y,
}


def simple_iteration_method_for_systems(f, g, a_1, b_1, a_2, b_2, x0, y0, accuracy, max_iterations):
    phi_f = lambdify([x, y], phi[f])
    phi_g = lambdify([x, y], phi[g])
    iterations = 0
    q = abs(lambdify([x, y], Derivative(phi[f], x).doit())(a_1, a_2)) + abs(lambdify([x, y],Derivative(phi[f], y).doit())(a_1, a_2))
    vector = [[], []]
    df_x = lambdify([x, y], Derivative(phi[f], x).doit())
    df_y = lambdify([x, y], Derivative(phi[f], y).doit())
    dg_x = lambdify([x, y], Derivative(phi[g], x).doit())
    dg_y = lambdify([x, y], Derivative(phi[g], y).doit())
    for i in np.arange(a_1, b_1, accuracy):
        for j in np.arange(a_2, b_2, accuracy):
            if abs(df_x(i, j)) + abs(df_y(i, j)) > q:
                q = abs(df_x(i, j)) + abs(df_y(i, j))
            if abs(dg_x(i, j)) + abs(dg_y(i, j)) > q:
                q = abs(dg_x(i, j)) + abs(dg_y(i, j))
            if q >= 1:
                print("The convergence condition is not met")
                return None, None, None
    xi, yi = x0, y0
    x_prev, y_prev = xi + accuracy + 1, yi + accuracy + 1
    while (iterations < max_iterations) and (abs(x_prev - xi) > accuracy) and (abs(y_prev - yi) > accuracy):
        iterations += 1
        buf_x, buf_y = xi, yi
        xi, yi = phi_f(buf_x, buf_y), phi_g(buf_x, buf_y)
        x_prev, y_prev = buf_x, buf_y
        vector[0].append(abs(xi - x_prev))
        vector[1].append(abs(yi - y_prev))
    return xi, yi, iterations, vector
