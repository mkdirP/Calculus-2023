import numpy as np


def runge_kutta(equation, x, y, h):
    k1 = h * equation(x, y)
    k2 = h * equation(x + h / 2, y + k1 / 2)
    k3 = h * equation(x + h / 2, y + k2 / 2)
    k4 = h * equation(x + h, y + k3)
    return y + (k1 + 2 * k2 + 2 * k3 + k4) / 6


def runge_kutta_method(equation, x0, xn, y0, h, accuracy, for_miln=False):
    print("Runge-Kutta method")
    y_prev = y0
    y_curr = 0
    y_curr_2 = accuracy + 1
    print("h || y_curr || y_curr_2 || abs(y_curr - y_curr_2) || accuracy")
    while abs(y_curr - y_curr_2) > accuracy:
        y_curr = runge_kutta(equation, x0, y_prev, h)
        y_curr_2 = runge_kutta(equation, x0, y_prev, h / 2)
        y_curr_2 = runge_kutta(equation, x0 + h / 2, y_curr_2, h / 2)
        print(f"{round(h, 6)} || {round(y_curr, 6)} || {round(y_curr_2, 6)} || {round(abs(y_curr - y_curr_2), 6)} || {accuracy}")
        h /= 2
    h *= 2
    x = np.arange(x0, xn + h, h)
    y = [0 for i in range(len(x))]
    y[0] = y0
    for i in range(1, len(x)):
        y[i] = runge_kutta(equation, x[i - 1], y[i - 1], h)
    print("------------------------------------")
    return y, x
