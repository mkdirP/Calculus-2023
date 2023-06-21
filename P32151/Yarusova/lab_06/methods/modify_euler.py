import numpy as np


def euler(equation, x_prev, x, y_prev, h):
    return y_prev + h / 2 * (equation(x_prev, y_prev) + equation(x, y_prev + h * equation(x_prev, y_prev)))


def modify_euler_method(equation, x0, xn, y0, h, accuracy):
    x = np.arange(x0, xn + h, h)
    y = np.zeros(len(x))
    y[0] = y0
    for i in range(1, len(x)):
        y[i] = euler(equation, x[i - 1], x[i], y[i - 1], h)
    return y, x
