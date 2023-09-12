import numpy as np
from math import ceil
from methods.runge_kutta import runge_kutta_method


def prediction(equation, x, y, h, i):
    return y[i - 4] + 4 * h / 3 * (2 * equation(x[i - 3], y[i - 3]) - equation(x[i - 2], y[i - 2]) + 2 * equation(x[i - 1], y[i - 1]))


def correction(equation, x, y, h, i, y_pred):
    return y[i - 2] + h / 3 * (equation(x[i - 2], y[i - 2]) + 4 * equation(x[i - 1], y[i - 1]) + equation(x[i], y_pred))


def miln_method(equation, x0, xn, y0, h, accuracy):
    print("Miln method")
    n = ceil((xn - x0) / h) + 1
    if n < 4:
        print("Error: h is too big, not enough points for Miln method")
        return None, None
    x = [x0 + i * h for i in range(n)]
    runge_kutta_y, runge_kutta_x = runge_kutta_method(equation, x[0], x[3], y0, h, accuracy, True)
    y = runge_kutta_y[:4]
    print("Prediction || Correction || abs(Prediction - Correction) || accuracy")
    for i in range(4, n):
        y_pred = prediction(equation, x, y, h, i)
        y_corr = correction(equation, x, y, h, i, y_pred)
        print(f"{round(y_pred, 6)} || {round(y_corr, 6)} || {round(abs(y_pred - y_corr), 6)} || {accuracy}")
        while abs(y_corr - y_pred) > accuracy:
            y_pred = y_corr
            y_corr = correction(equation, x, y, h, i, y_pred)
            print(f"{round(y_pred, 6)} || {round(y_corr, 6)} || {round(abs(y_pred - y_corr), 6)} || {accuracy}")
        y.append(y_corr)
    print("------------------------------------")
    return y, x
