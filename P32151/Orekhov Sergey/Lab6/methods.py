import math
import sys

import numpy as np


def euler(f, x0, y0, h, xn):
    X = []
    Y = []
    X.append(x0)
    Y.append(y0)
    while x0 < xn:
        y0 = y0 + h * f(x0, y0)
        x0 += h
        X.append(x0)
        Y.append(y0)
    return X, Y


def fourth_order_runge_kutta(f, x0, y0, h, xn):
    X, Y = [], []
    X.append(x0)
    Y.append(y0)
    while x0 < xn:
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h / 2, y0 + k1 / 2)
        k3 = h * f(x0 + h / 2, y0 + k2 / 2)
        k4 = h * f(x0 + h, y0 + k3)
        x0 += h
        y0 = y0 + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        X.append(x0)
        Y.append(y0)
    return X, Y


def milna(f, x, y, h, xn, eps):
    xnn = x + h * 4
    X, Y = fourth_order_runge_kutta(f, x, y, h, xnn)
    F = []
    for i in range(4):
        F.append(f(X[i], Y[i]))

    # Prediction part:

    while X[-1] < xn:
        X.append(X[-1] + h)
        Y.append(Y[-4] + 4 * h / 3 * (2 * F[-3] - F[-2] + 2 * F[-1]))
        Fi = f(X[-1], Y[-1])
        y_correct = Y[-2] + h / 3 * (F[-2] + 4 * F[-1] - Fi)

        # Correction part:
        while abs(y_correct - Y[-1]) >= eps:
            Y[-1] = y_correct
            Fi = f(X[-1], y_correct)
            y_correct = Y[-2] + h / 3 * (F[-2] + 4 * F[-1] - Fi)
        Y[-1] = y_correct
        F[-1] = Fi
    return X, Y


def runge_rule(method, f, x0, y0, h, xn, p, eps=None):
    eps_array = []
    if eps is None:
        eps = 0.01
        X, Y1 = method(f, x0, y0, h, xn)
        Y2 = method(f, x0, y0, h / 2, xn)[1]
    else:
        X, Y1 = method(f, x0, y0, h, xn, eps)
        Y2 = method(f, x0, y0, h / 2, xn, eps)[1]

    for i in range(1, int(math.ceil((xn - x0) / h))):
        res = abs(Y1[i] - Y2[i]) / (2 ** p - 1)
        eps_array.append(res)

    if len(eps_array) == 0:
        sys.exit("Bad interval! Expected more elements")
    is_optimal = max(eps_array) < eps
    eps_array = np.array(eps_array)
    return eps_array.mean(), "h is OK" if is_optimal else "h is NOT OK"
